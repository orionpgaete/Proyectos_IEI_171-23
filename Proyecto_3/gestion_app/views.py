from django.shortcuts import render
from gestion_app.models import Productos

# Create your views here.

def busqueda_prd(request):
    return render(request, "busqueda.html")


def buscar(request):
    if request.GET["prd"]:
        producto = request.GET["prd"]
        prodDB = Productos.objects.filter(nombre__icontains=producto)

        return render(request, "resultado.html", {"prodW": prodDB, "query": producto})
    else:
        mensaje = "No hay nada de nada"
    
