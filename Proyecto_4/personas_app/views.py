from django.shortcuts import render
from personas_app import models

# Create your views here.

def traedatos_persona(request):
    persona = models.Empleados.objects.all()
    data = {'perso' : persona}
    return render(request, 'empleados.html', data)