from ast import Name
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.inicio , name="inicio"),
    path("aboutUs",views.aboutUS, name ="sobreNosotros"),
    path("contacto",views.contacto , name="contacto"),
    path("suba_su_cv",views.subirCv , name ="subirCv"),
    path("ingresar",views.login_request , name = "ingresar" ),
    path("registrar",views.registrar, name ="registrar"),
    path("altaServicio",views.altaServicio , name ="altaServicio"),
    path("logout",LogoutView.as_view( template_name = "logout.html") , name="Logout"),
    path("prueba",views.prueba),
    path("servicios",views.servicios, name="servicios"),
    path("buscarServicios",views.buscar_servicio, name="buscarServicio"),
    path("buscar",views.buscar),
    path("eliminar_servicio/<int:id>",views.eliminar_servicio, name="eliminar_servicio"),
    path("editar_servicio/<int:id>", views.editar_servicio, name="editar_servicio"),
    path("editar_servicio/", views.editar_servicio, name="editar_servicio"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil"),
    path("servicios_usuario", views.servicios_usuario, name="servicios_usuario"),
    path("post", views.post, name="post"),
    path("subirPost",views.subir_post,name="subirPost")
]
