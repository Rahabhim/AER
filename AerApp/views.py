from django.shortcuts import render, HttpResponse
from publicaciones.models import Publicacion

# Create your views here.

def home(request):
    return render(request, "AerApp/home.html")

def servicios(request):
    return render(request, "AerApp/servicios.html")

def equipo(request):
    return render(request, "AerApp/equipo.html")

def publicaciones(request):
    publicaciones=Publicacion.objects.all()
    return render(request, "AerApp/publicaciones.html", {"publicaciones": publicaciones})

def contacto(request):
    return render(request, "AerApp/contacto.html")
