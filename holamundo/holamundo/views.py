from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1>Hola Alumnos bienvenidos al DJANGO¡¡¡¡¡</h1>")

def nosvemos(request):
    return HttpResponse("Nos velmont")