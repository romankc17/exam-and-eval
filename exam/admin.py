from django.contrib import admin

# Register your models here.
from .models import Exam, Question, Choice

admin.site.register((Exam, Question, Choice))
