from django.db import models

# Modelo Película
class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    director = models.CharField(max_length=40)
    genero = models.CharField(max_length=20)
    duracion = models.FloatField()

# Modelo Serie
class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    temporadas = models.IntegerField()

class futbol(models.Model):
    equipo_local = models.CharField(max_length=40)
    equipo_visitante = models.CharField(max_length=40)
    resultado = models.CharField(max_length=40)
    fecha = models.DateField()
    
    