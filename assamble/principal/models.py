from django.db import models

# Create your models here.

class Servicio(models.Model):
    
    nombre_servicio = models.CharField(max_length=40)
    precio_servicio = models.IntegerField()
    calidad_servicio = models.CharField(max_length=40)
    descripcion_producto = models.CharField(max_length=500)