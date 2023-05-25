from django.urls import path
from . import views

urlpatterns=[
    path('', views.iniciogroups, name='Inicio Grupo'),
    path('groupslistas', views.groupslistas, name='Lista de Grupos')
]