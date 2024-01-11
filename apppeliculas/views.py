from django.shortcuts import render
from apppeliculas.models import Serie, Pelicula
# Create your views here.

def ver_serie(request):

    mis_seriees = Serie.objects.all()

    info = {"series":mis_seriees}
    

    return render(request, "series.html",info)













""""
def agregar_serie(request):
    
    serie1 = Serie (nombre="The 100", año=2014,temporadas=7)
    serie1.save()
    return HttpResponse("se agrego una serie... ")

def agregar_pelicula(request):
    
    Pelicula1 = Pelicula (nombre="En Busca De La Felicidad", año=2006, director="Gabriele Muccino",
                           genero=" drama biográfico", duracion=1.57)
    Pelicula1.save()
    return HttpResponse("se agrego una pelicula... ")
"""