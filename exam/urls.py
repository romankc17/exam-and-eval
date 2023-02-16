# project/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.exam_list, name='index'),
    path('exam/create/', views.exam_create, name='exam_create'),
    path('exam/<int:pk>/', views.exam_detail, name='exam_detail'),
    path('results/<str:username>/', views.results, name='results'),

]
