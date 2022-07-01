from django.shortcuts import render

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