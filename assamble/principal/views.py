from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from principal.models import Servicio, Avatar
from .forms import Alta_servicio, CustomUserCreationForm, UserEditForm

# Create your views here.

def prueba(request):
    return render(request,"prueba3.html")

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

def servicios_usuario(request):
    servicios = Servicio.objects.all()
    dicc = {"servicios": servicios}
    plantilla = loader.get_template("servicios_usuario.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def inicio_usuario(request):
    return render(request, "padre_usuario.html")

def servicios(request):
    servicios = Servicio.objects.all()
    dicc = {"servicios": servicios}
    plantilla = loader.get_template("servicios.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def buscar_servicio(request):

    return render(request, "buscar_servicio.html")

def buscar(request):

    if request.GET['nombre_servicio']:
        nombre_servicio = request.GET['nombre_servicio']
        servicios = Servicio.objects.filter(nombre_servicio__icontains = nombre_servicio)
        return render(request, "resultado_busqueda.html", {"servicios": servicios})
    else:
        return HttpResponse("Campo vacío")

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data =request.POST)
        
        if form.is_valid():
            usuario =form.cleaned_data.get("username")
            
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password =contra)
            
            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "padre_usuario.html", {"url": avatares[0].imagen.url})
            
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

def eliminar_servicio(request, id):

    servicio = Servicio.objects.get(id = id)
    servicio.delete()

    servicio = Servicio.objects.all()

    return render(request, "servicios.html", {"servicios": servicio})

def editar_servicio(request, id):
    
    servicio = Servicio.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Alta_servicio(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            servicio.nombre_servicio = datos['nombre_servicio']
            servicio.precio_servicio = datos['precio_servicio']
            servicio.calidad_servicio = datos['calidad_servicio']
            servicio.descripcion_producto = datos['descripcion_producto']
            servicio.save()

            servicio =Servicio.objects.all()
            return render(request, "servicios.html", {"servicios": servicio})
    else:
        mi_formulario = Alta_servicio(initial={'nombre_servicio': servicio.nombre_servicio, 'precio_servicio': servicio.precio_servicio, 'calidad_servicio': servicio.calidad_servicio, 'descripcion_producto': servicio.descripcion_producto})

    return render(request, "editar_servicio.html", {"mi_formulario": mi_formulario, "servicio":servicio})




def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(data =request.POST)

        if form.is_valid():
            
            form.save()
            return HttpResponse("Usuario creado")
        
    form = UserCreationForm()
    return render( request , "registrar.html" , {"form":form, "servicios": servicios})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request,"main.html")

    else:
        miFormulario = UserEditForm(initial= {'email': usuario.email})
    
    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})



