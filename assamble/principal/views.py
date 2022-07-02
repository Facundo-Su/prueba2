from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate

from principal.models import Servicio
from .forms import Alta_servicio, CustomUserCreationForm

# Create your views here.

def inicio(request):
    return render(request , "main.html")

def aboutUS(request):
    return render(request , "aboutUs.html")

def contacto(request):
    return render(request , "contacto.html")

def subirCv(request):
    return render(request,"subir-cv.html")

def ingresar(request):
    return render(request , "ingresar.html")

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data =request.POST)
        
        if form.is_valid():
            usuario =form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password =contra)
            
            if user is not None:
                login(request,user)
                return render(request ,"ingresadoCorrectamente.html",{"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"usuario incorrecto")
    
    form = AuthenticationForm()
    context={'form':form}
    return render(request , "ingresar2.html",context)


def altaServicio(request):

    if request.method =="POST":
        mi_formulario = Alta_servicio( request.POST )

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data          
            servicio = Servicio( nombre_servicio=datos['nombre_servicio'], precio_servicio=datos['precio_servicio'], calidad_servicio=datos['calidad_servicio'], descripcion_producto=datos['descripcion_producto'])
            servicio.save()
            return render( request , "alta_servicio.html")
        
        return HttpResponse("hola")

    return render( request, "alta_servicio.html")

def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(data =request.POST)

        if form.is_valid():
            
            form.save()
            return HttpResponse("Usuario creado")
        
    form = UserCreationForm()
    return render( request , "registrar.html" , {"form":form})