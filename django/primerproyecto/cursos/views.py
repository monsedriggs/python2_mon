from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def iniciocursos(request):
    return HttpResponse("<h1>Lista de Cursos</h1>")

def cursoslistas(request):
    return render(request, 'paginas/cursoslista.html')