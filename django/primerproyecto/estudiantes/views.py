from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def iniciostudents(request):
    return HttpResponse("<h1>Lista de Estudiantes</h1>")

def studentlistas(request):
    return render(request, 'paginas/studentlista.html')