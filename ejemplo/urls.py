from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index,name='index.html'),
    path('libros/listar',views.listar_libros, name='listar_libros'),
    path('libros/<int:id_libros>/', views.dame_libro, name='dame_libro'),
    path('libros/listar/<int:anyo_libros>/<int:mes_libros>',views.dame_libros_fecha, name="dame_libros_fecha"),
    path('libros/listar/<str:idioma>/', views.dame_libros_idioma,name="dame_libros_idioma"),
    path('biblioteca/<int:id_biblioteca>/libros/<str:descripcion_libros>',views.dame_libros_biblioteca, name="dame_libros_biblioteca"),
    path('ultimo-cliente-libro/<int:libro>',views.dame_ultimo_cliente_libro,name='ultimo-cliente-libro'),
    re_path(r"^filtro[0-9]$", views.libros_no_prestados, name="libros_no_prestados"),
]
