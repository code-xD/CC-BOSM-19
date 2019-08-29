from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('team_register', views.team_register, name='team_register'),
    path('question_details/', views.question_details, name='question_details'),
    path('check_question_answer/', views.check_question_answer, name='check_question_answer'),
]