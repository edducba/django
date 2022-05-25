
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
#from proyecto1.views import probandotemplate 

from proyecto1.views import saludo 

#from proyecto1.views import saludo
from proyecto1.views import DiaDeHoy
from proyecto1.views import segunda_vista
from proyecto1.views   import probandotemplate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',saludo),
    path('second_view/',segunda_vista),
    path('today/',DiaDeHoy),
    path('probandotemplate/', probandotemplate),    
]

 