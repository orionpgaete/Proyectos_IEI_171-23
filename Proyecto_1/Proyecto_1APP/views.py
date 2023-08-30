from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def saludo(request):
    return HttpResponse('Hola a todos')


def renderTemplate(request):
    data = {"nombre": "Pedro"}
    return render(request, 'templateAPP1/plantilla.html', data)

def infoUsuario(request):
    data = {"id": "123", "nombre":"Pedro", "email":"pedro@gmail.com"}
    return render(request, 'templateAPP1/userInfoTemplate.html', data)