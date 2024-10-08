from django.contrib import admin
from .models import Cliente, Biblioteca, datosCliente, Autor, Libros

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Biblioteca)
admin.site.register(datosCliente)
admin.site.register(Autor)
admin.site.register(Libros)

