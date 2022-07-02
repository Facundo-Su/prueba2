from django import forms

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass

class Alta_servicio(forms.Form):
    
    nombre_servicio = forms.CharField(max_length=40)
    precio_servicio = forms.FloatField()
    calidad_servicio = forms.CharField(max_length=40)
    descripcion_producto = forms.CharField(max_length=500)
