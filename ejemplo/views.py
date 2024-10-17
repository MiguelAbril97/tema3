from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def index (request):
    return render (request, 'index.html')

def listar_libros(request):
    libros = Libros.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.all()
    return render (request, 'libro/lista.html', {'libros_mostrar':libros})

def dame_libro(request,id_libros):
    libro=Libros.objects.select_related("biblioteca").prefetch_related("autores").get(id=id_libros)
    return render(request, 'libro/libro.html', {"libro_mostrar":libro})

def dame_libros_fecha(request, anyo_libros,mes_libros):
     libros = Libros.objects.select_related('biblioteca').prefetch_related('autores')
     libros = libros.filter(fecha_publicacion__year=anyo_libros,fecha_publicacion__month=mes_libros)
     return render(request, 'libro/lista.html',{"libros_mostrar": libros})

def dame_libros_idioma(request, idioma):
    libros = Libros.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(Q(tipo=idioma) | Q(tipo="ES")).order_by("fecha_publicacion")
    return render(request, 'libro/lista.html',{"libros_mostrar": libros})

def dame_libros_biblioteca (request, id_biblioteca, descripcion_libros):
    libros=Libros.objects.select_related('biblioteca').prefetch_related('autores')
    libros = libros.filter(biblioteca = id_biblioteca).filter(descripcion__contains=descripcion_libros)
    