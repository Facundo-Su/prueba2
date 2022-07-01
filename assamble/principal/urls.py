from django.urls import path
from . import views
urlpatterns = [
    path("",views.inicio , name="inicio"),
    path("aboutUs",views.aboutUS, name ="sobreNosotros"),
    path("contacto",views.contacto , name="contacto"),
    path("suba_su_cv",views.subirCv , name ="subirCv"),
    path("ingresar",views.ingresar , name = "ingresar" )
]
