from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicioprofes, name='Inicio Profesores'),
    path('profeslistas', views.profeslistas, name='Lista de Profesores')
]