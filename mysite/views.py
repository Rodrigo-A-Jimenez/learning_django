import datetime
from django.http import HttpResponse

def saludo(request):
    txt = "<h1>Hola mundo</h1>"
    return HttpResponse(txt)

def despedida(request):
    return HttpResponse("Adios mundo")

def date(request):
    actualDate = datetime.datetime.now()
    txt = "<h1>Fecha actual: %s</h1>" % actualDate
    return HttpResponse(txt)

def squadArea(request, squad):
    txt = "<h1>El área del squad %s es: %s</h1>" % (squad, squad * squad)
    return HttpResponse(txt)