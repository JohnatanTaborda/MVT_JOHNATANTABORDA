from django.shortcuts import render
from .models import Familia, Familiares
from django.http import HttpResponse
from django.template import Template, Context, loader

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
    
    # Datos_familiares = (nombre1="John", dni1=1036, nacimiento1="1988-1-24", nombre2="Lau", dni2=1039, nacimiento2="1991-9-15", nombre3="Gladis", dni3=4357, nacimiento3="1973-11-11")
    
    Nombre1="John"
    Dni1=int(1036)
    Nacimiento1="1988-1-24"
    Nombre2="Lau"
    Dni2=int(1039)
    Nacimiento2="1991-9-15"
    Nombre3="Gladis"
    Dni3=int(4357)
    Nacimiento3="1973-11-11"
   
    familiares = Familiares(nombre1=Nombre1, dni1=Dni1, nacimiento1=Nacimiento1, nombre2=Nombre2, dni2=Dni2, nacimiento2=Nacimiento2, nombre3=Nombre3, dni3=Dni3, nacimiento3=Nacimiento3)
    familiares.save()
    
    #archivo = open("./Templates/Template1.html")
    #template = Template(archivo.read())
    #archivo.close()
    
    Diccionario = { "nombre1":Nombre1, "identificación1":Dni1, "f_nacimiento1":Nacimiento1, 
                   "nombre2":Nombre2, "identificación2":Dni2, "f_nacimiento2":Nacimiento2,
                   "nombre3":Nombre3, "identificación3":Dni3, "f_nacimiento3":Nacimiento3
                   }
    
    plantilla=loader.get_template('Template1.html')
    
    #contexto = Context(Diccionario)
    
    documento = plantilla.render(Diccionario)
    
    return HttpResponse(documento) 