from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    fono = models.IntegerField()
    direccion = models.CharField(max_length=60)
