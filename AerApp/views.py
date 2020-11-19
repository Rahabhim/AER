from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Inicio")

def servicios(request):
    return HttpResponse("Servicios")

def equipo(request):
    return HttpResponse("Equipo")

def publicaciones(request):
    return HttpResponse("Publicaciones")

def contacto(request):
    return HttpResponse("Contacto")
