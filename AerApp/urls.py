from django.urls import path

from AerApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="Inicio"),
    path("servicios", views.servicios, name="Servicios"),
    path("equipo", views.equipo, name="Equipo"),
    path("publicaciones", views.publicaciones, name="Publicaciones"),
    path("contacto", views.contacto, name="Contacto"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
