from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def iniciogroups(request):
    return HttpResponse("<h1>Lista de Grupos</h1>")

def groupslistas(request):
    return render(request, 'paginas/groupslista.html')