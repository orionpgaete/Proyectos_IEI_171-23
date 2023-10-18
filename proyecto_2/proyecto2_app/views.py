from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'proyecto2_app/index.html')

def electronica(request):
    data = {"titulo":"Electronica", "foto1":"electronica1.jpg", "foto2":"electronica2.jpg", "foto3":"electronica3.jpg", "producto1":"Mouse Inalambrico", "producto2": "Luz led embutida", "producto3":"Tester Digital"}
    return render(request, 'proyecto2_app/producto.html', data)

def juguete(request):
    data = {"titulo":"Juguete" , "foto1":"juguete1.jpg", "foto2":"juguete2.jpg", "foto3":"juguete3.jpg", "producto1":"Juego Didactico", "producto2": "Autos", "producto3":"Muñeca Grande"}
    return render(request, 'proyecto2_app/producto.html', data)