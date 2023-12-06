from django.db import models

# Create your models here.
class Proyecto(models.Model):
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioriodad = models.IntegerField()