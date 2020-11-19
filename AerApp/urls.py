from django.urls import path

from AerApp import views

urlpatterns = [
    path("", views.home, name="Inicio"),
    path("servicios", views.servicios, name="Servicios"),
    path("equipo", views.equipo, name="Equipo"),
    path("publicaciones", views.publicaciones, name="Publicaciones"),
    path("contacto", views.contacto, name="Contacto"),
]
