from cgitb import html
from django.template import Template, Context
#from django.template import loader 

import datetime

from multiprocessing import context

  
 

from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola Bienvenido')


def segunda_vista(request):
    return HttpResponse('Nueva ventana ')

def DiaDeHoy(request):
    dia= datetime.datetime.now()
    texto = 'Hoy es: {}'.format(dia)    
    return HttpResponse(texto)
# definiendo la apertura del programa 

def probandotemplate(self):
    miHtml = open('/Users/edducba/Desktop/django/proyecto1/proyecto1/plantillas/template1.html')
    
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
    






