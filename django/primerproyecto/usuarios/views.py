from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def iniciousers(request):
    return HttpResponse("<h1>Lista de Usuarios</h1>")

def userslistas(request):
    return render(request, 'paginas/userslista.html')