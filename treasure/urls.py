from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('googlesignin/', views.renderLogin, name='render-login'),
    path('profile/', views.renderToken, name='render-token'),
    path('<str:filename>', views.renderFile, name='render-file'),
    # path('team_register', views.team_register, name='team_register'),
    path('get_pin/', views.getData, name='get-data-debug'),
    path('join_team/', views.join_team, name='join_team'),
    path('question_details/', views.question_details, name='question_details'),
    path('check_question_answer/', views.check_question_answer, name='check_question_answer'),
]
