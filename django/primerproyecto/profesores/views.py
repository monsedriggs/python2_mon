from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicioprofes(request):
    return HttpResponse("<h1>Lista de Profesores</h1>")

def profeslistas(request):
    return render(request, 'paginas/profeslista.html')