from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('team_register', views.team_register, name='team_register')
]