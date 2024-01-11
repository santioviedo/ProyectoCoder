from django.db import models

class camiseta (models.Model):
    equipo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    año = models.IntegerField()
    tipo = models.CharField(max_length=30)

class short (models.Model):
    equipo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    año = models.IntegerField()
    tipo = models.CharField(max_length=30)

class botines (models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)