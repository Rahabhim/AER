from django.shortcuts import render
from .models import Publicacion

# Create your views here.


def publicaciones(request):
    publicaciones=Publicacion.objects.all()
    return render(request, "publicaciones/publicaciones.html", {"publicaciones": publicaciones})
