from django.shortcuts import render
from .models import Familia, Familiares
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def familia(request):
    
    familia1= Familia(nombre="John", dni=1036, nacimiento="1988-1-24")
    familia2= Familia(nombre="Lau", dni=1039, nacimiento="1991-9-15")
    familia3= Familia(nombre="Gladis", dni=4357, nacimiento="1973-11-11")
    
    familia1.save()
    familia2.save()
    familia3.save()
    
    Respuesta1= "Familiar 1 guardado: "+familia1.nombre+" "+str(familia1.dni)+" "+str(familia1.nacimiento)+" Familiar 2 guardado: "+familia2.nombre+" "+str(familia2.dni)+" "+str(familia2.nacimiento)+" Familiar 3 guardado: "+familia3.nombre+" "+str(familia3.dni)+" "+str(familia3.nacimiento) 
    
    return HttpResponse(Respuesta1)


def familiares(request):
    
    familiares = Familiares(nombre1="John", dni1=1036, nacimiento1="1988-1-24", nombre2="Lau", dni2=1039, nacimiento2="1991-9-15", nombre3="Gladis", dni3=4357, nacimiento3="1973-11-11" )
    familiares.save()
    
    archivo = open("./Templates/Template1.html")
    template = Template(archivo.read())
    archivo.close()
    contexto = Context(familiares)
    documento = template.render(contexto)
    
    return HttpResponse(documento)