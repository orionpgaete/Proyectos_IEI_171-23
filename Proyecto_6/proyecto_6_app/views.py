from django.shortcuts import render, redirect
from proyecto_6_app.models import Proyecto
from .forms import FormProyecto

# Create your views here.

def index(request):
    return render(request, 'index.html')


def listadoproyecto(request):
    proye = Proyecto.objects.all()
    data = {'proyec': proye}
    return render(request, 'proyectos.html', data)

def agregarproyecto(request):
    form = FormProyecto()

    if (request.method == 'POST'):
        form = FormProyecto(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)

    data ={'form' : form}
    return render(request, 'agregar.html', data)

def eliminarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    pro.delete()
    return redirect('/proyectos')

def modificarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=pro)

    if (request.method == 'POST'):
        form = FormProyecto(request.POST, instance=pro)
        if (form.is_valid()):
            form.save()
        return index(request)

    data ={'form' : form}
    return render(request, 'agregar.html', data)



