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


def calculaedad(request, edadactual, agno):
    #edadactual = 18
    periodo = agno - 2023
    edadfutura = edadactual + periodo
    docum = """
            <html>
                <body>
                    <h1>En el año %s tendras %s años</h1>
                </body>
            </html>""" % (agno, edadfutura)
    return HttpResponse(docum)
