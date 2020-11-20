from django.shortcuts import render
from .models import Post, Categoria


# Create your views here.


def publicaciones(request):
    posts=Post.objects.all()
    return render(request, "blog/publicaciones.html", {"posts": posts})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria)
    return render(request, "blog/categorias.html", {"categoria": categoria})
