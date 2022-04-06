
import datetime
from django.conf import settings
from django.http import HttpResponse
from django.template import loader

def main(request):
    
    template = loader.get_template('base.html')
    context = {}
    return HttpResponse(template.render(context))

def saludo(request):
    name = "Rodrigo Andres"
    lastName = "Jimenez Huanca"
    date = datetime.datetime.now()
    
    template = loader.get_template('saludo.html')
    context = {'name': name, 'lastName': lastName, 'date': date.date()}
    return HttpResponse(template.render(context))

def despedida(request):
    return HttpResponse("Adios mundo")

def date(request):
    actualDate = datetime.datetime.now()
    txt = "<h1>Fecha actual: %s</h1>" % actualDate
    return HttpResponse(txt)

def squadArea(request, squad):
    page = loader.get_template('squadArea.html')
    parameters = {'squad': squad, 'area': squad**2, 'squadPX':15*squad, 'textArea': 4*squad}
    txt = "<h1>El área del squad %s es: %s</h1>" % (squad, squad * squad)
    return HttpResponse(page.render(parameters))