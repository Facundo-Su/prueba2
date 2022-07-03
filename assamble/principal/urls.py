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
]
