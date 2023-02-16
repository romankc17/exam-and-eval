from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Exam,Question,Choice,Enrollment
import datetime

def exam_list(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'exam/exam_list.html', context)

@login_required
def exam_detail(request, pk):
    if request.method == 'POST':
        exam = get_object_or_404(Exam, pk=pk)
        questions = Question.objects.filter(exam=exam)
        score = 0
        for question in questions:
            correct_answer = Choice.objects.filter(question=question,is_correct=True).first()
            print('correct_answer: ',correct_answer)
            if request.POST.get('question-'+str(question.id)) == str(correct_answer.id):
                score += 1
        if Enrollment.objects.filter(user=request.user,exam=exam).exists():
            enrollment = Enrollment.objects.filter(user=request.user,exam=exam).first()
            enrollment.score = score
            enrollment.save()
        else:
            Enrollment.objects.create(user=request.user,exam=exam,score=score)
            
        return redirect('results', username=request.user.username)
    exam = get_object_or_404(Exam, pk=pk)
    questions = Question.objects.filter(exam=exam)
    return render(request, 'exam/exam_detail.html', {'exam': exam, 'questions': questions})

@login_required
def results(request, username):
    enrollments = Enrollment.objects.filter(user__username=username)
    print(enrollments)
    return render(request, 'exam/results.html', {'enrollments': enrollments})

@staff_member_required
def exam_create(request):
    if request.method == 'POST':
        exam = Exam.objects.create(
            exam_name=request.POST['exam_name'],
            description=request.POST['exam_description'],
        )
        qCounts = request.POST['questionCounter']
        print(qCounts)
        for count in range(1,int(qCounts)+1):
            try:
                question_text = request.POST['question'+str(count)]
            except:
                continue
            question = Question.objects.create(exam=exam,question_text=question_text)
            correct_choice = request.POST.get('correct-answer'+str(count))
            print(correct_choice)
            for i in range(1,5):
                choice_text = request.POST['choice'+str(count)+str(i)]
                choice=Choice(question=question,choice_text=choice_text)
                if correct_choice==str(i):
                    choice.is_correct=True
                choice.save()
            
            
        return redirect('index')
    
    return render(request, 'exam/exam_create.html')