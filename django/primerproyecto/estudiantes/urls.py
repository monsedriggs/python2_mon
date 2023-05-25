from django.urls import path
from . import views

urlpatterns=[
    path('', views.iniciostudents, name='Inicio Estudiantes'),
    path('studentlistas', views.studentlistas, name='Lista de Estudiantes')
]