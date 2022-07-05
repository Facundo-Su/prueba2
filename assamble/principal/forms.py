from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    pass

class Alta_servicio(forms.Form):
    
    nombre_servicio = forms.CharField(max_length=40)
    precio_servicio = forms.FloatField()
    calidad_servicio = forms.CharField(max_length=40)
    descripcion_producto = forms.CharField(max_length=500)

class Alta_Mensaje(forms.Form):

    titulo = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    mensaje = forms.CharField(max_length=500)
    comentario = forms.CharField(max_length=500)

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k: "" for k in fields}
    

