import datetime
from django.http import HttpResponse

def saludo(request):
    docum = """
            <html>
                <body>
                    <h1>Hola Alumnos bienvenidos al DJANGO¡¡¡¡¡</h1>
                </body>
            </html>"""
    return HttpResponse(docum)

def nosvemos(request):
    return HttpResponse("Nos velmont")

def fechaactual(request):
    fecha_actual=datetime.datetime.now()
    docum = """
            <html>
                <body>
                    <h1>La fecha y hora es %s</h1>
                </body>
            </html>""" % fecha_actual
    return HttpResponse(docum)