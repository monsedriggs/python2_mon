from django.urls import path
from . import views

urlpatterns=[
    path('', views.iniciocursos, name='Inicio Cursos'),
    path('cursoslistas', views.cursoslistas, name='Lista de Cursos')
]