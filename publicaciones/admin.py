from django.contrib import admin
from .models import Publicacion

# Register your models here.

class PublicacionAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')


admin.site.register(Publicacion, PublicacionAdmin)
