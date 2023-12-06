from django.http import JsonResponse
from django.shortcuts import render
from proyecto_7_app import models

# Create your views here.

def empleadosView(request):
    emp = {
        'id' : 123,
        'nombre' : 'Juanito',
        'email' : 'ju@inacap.cl',
        'sueldo' : '10000000'
    }
    return JsonResponse(emp)


def empleadosView_DB(request):
    empl = models.Empleados.objects.all()
    data = {'emple' : list(empl.values('nombre', 'sueldo'))}
    return JsonResponse(data)
