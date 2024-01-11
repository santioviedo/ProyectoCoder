from django.shortcuts import render
from apptiendafutbol.models import *
from apptiendafutbol.forms import *


def inicio(request):
   return render(request, "inicio.html")


def pedir_camiseta(request):
    if request.method=="POST":

       info_formulario = camisetaformulario(request.POST)

       if info_formulario.is_valid():
            info = info_formulario.cleaned_data

            nueva_camisetas = camiseta(equipo=info["equipo"], talle=info["talle"], año=info["año"],tipo=info["tipo"])
            nueva_camisetas.save()
           
            return render(request,"inicio.html")
    else:
     
        info_formulario = camisetaformulario() 

    return render(request,"crear_camisetas.html",{"formu":info_formulario})

#---------------------------------------------------------------------------------------------------

def pedir_shorts(request):

    if request.method=="POST":

       info_formulario = shortformulario(request.POST)

       if info_formulario.is_valid():          
            info = info_formulario.cleaned_data

            nuevo_shorts = short(equipo=info["equipo"], talle=info["talle"], año=info["año"],tipo=info["tipo"])
            nuevo_shorts.save()
           
            return render(request,"inicio.html")
    else:
     info_formulario = shortformulario() #aqui creamos un formulario vacio

    return render(request,"crear_shorts.html",{"formu":info_formulario})


#------------------------------------------------------------------------------------------

def pedir_botines(request):

    if request.method=="POST":

       info_formulario = botinesformulario(request.POST)

       if info_formulario.is_valid():
          
            info = info_formulario.cleaned_data

            nuevos_botines = botines(marca=info["marca"], modelo=info["modelo"], talle=info["talle"], )            
            nuevos_botines.save()
           
            return render(request,"inicio.html")
    else:
     info_formulario = botinesformulario() 

    return render(request,"crear_botines.html",{"formu":info_formulario})














