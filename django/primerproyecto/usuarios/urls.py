from django.urls import path
from . import views

urlpatterns=[
    path('', views.iniciousers, name='Inicio Usuarios'),
    path('userslistas', views.userslistas, name='Lista de Usuarios')
]