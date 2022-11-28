from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    nacimiento = models.DateField()


class Familiares(models.Model):
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    nombre3 = models.CharField(max_length=50)
    dni1 = models.IntegerField()
    dni2 = models.IntegerField()
    dni3 = models.IntegerField()
    nacimiento1 = models.DateField()
    nacimiento2 = models.DateField()
    nacimiento3 = models.DateField()
    