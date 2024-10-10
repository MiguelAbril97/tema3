from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Biblioteca (models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    
class Autor (models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200, blank=True)
    edad = models.IntegerField(null=True)

class Libros(models.Model):
    IDIOMAS = [
        ("ES", "Español"),
        ("EN", "Inglés"),
        ("FR", "Francés"),
        ("IT", "Italiano"),
    ]

    nombre = models.CharField(max_length=200)
    tipo =models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default="ES",
    )
    
    autores=models.ManyToManyField(Autor)
    
    descripcion = models.TextField()
    fecha_publicacion=models.DateField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete = models.CASCADE)

class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    puntos = models.FloatField(default=5.0, db_column='puntos_biblioteca')
    libros=models.ManyToManyField(Libros, through='Prestamos', related_name='libros')
    libros_preferidos=models.ForeignKey(Libros,on_delete= models.CASCADE ,related_name='favoritos')
    
class datosCliente (models.Model):
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    cliente = models.OneToOneField(Cliente, on_delete = models.CASCADE)
    
class Prestamos (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libros, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)


    