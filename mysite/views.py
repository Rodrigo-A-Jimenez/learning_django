
import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    name = "Rodrigo"
    lastName = "Jimenez"
    date = datetime.datetime.now()
    plantilla = open('mysite/templates/saludo.html')
    plt = Template(plantilla.read())
    plantilla.close()
    ctx = Context({'name': name, 'lastName': lastName, 'date': date.date()})
    doc = plt.render(ctx)
    return HttpResponse(doc)

def despedida(request):
    return HttpResponse("Adios mundo")

def date(request):
    actualDate = datetime.datetime.now()
    txt = "<h1>Fecha actual: %s</h1>" % actualDate
    return HttpResponse(txt)

def squadArea(request, squad):
    txt = "<h1>El área del squad %s es: %s</h1>" % (squad, squad * squad)
    return HttpResponse(txt)