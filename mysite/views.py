
import datetime
from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'base.html', context)

def saludo(request):
    name = "Rodrigo Andres"
    lastName = "Jimenez Huanca"
    date = datetime.datetime.now()
    
    context = {'name': name, 'lastName': lastName, 'date': date.date()}
    return render(request, 'saludo.html', context)

def despedida(request):
    return HttpResponse("Adios mundo")

def date(request):
    actualDate = datetime.datetime.now()
    txt = "<h1>Fecha actual: %s</h1>" % actualDate
    return HttpResponse(txt)

def squadArea(request, squad):
    parameters = {'squad': squad, 'area': squad**2, 'squadPX':15*squad, 'textArea': 4*squad}
    return render(request, 'squadArea.html', parameters) 