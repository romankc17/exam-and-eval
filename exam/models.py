from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    exam_name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.exam_name
    
    def question_count(self):
        return self.question_set.count()

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
    
   

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()
    date_enrolled = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username + ' - ' + self.exam.exam_name


