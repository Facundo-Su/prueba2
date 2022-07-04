from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servicio(models.Model):
    
    nombre_servicio = models.CharField(max_length=40)
    precio_servicio = models.IntegerField()
    calidad_servicio = models.CharField(max_length=40)
    descripcion_producto = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"Servicio: {self.nombre_servicio}"

class Avatar(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)