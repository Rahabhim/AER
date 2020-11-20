from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "AerApp/home.html")

def servicios(request):
    return render(request, "AerApp/servicios.html")

def equipo(request):
    return render(request, "AerApp/equipo.html")


def contacto(request):
    return render(request, "AerApp/contacto.html")
