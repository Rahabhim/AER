from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "AerApp/home.html")


def equipo(request):
    return render(request, "AerApp/equipo.html")

def publicaciones(request):
    return render(request, "AerApp/publicaciones.html")

def contacto(request):
    return render(request, "AerApp/contacto.html")
