from django.urls import path
from .views import IndexPageView
from . import views

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),  # Página de inicio
    path('lista_libros', views.lista_libro, name='lista_libros'), #lista de libros 
    path('ingresar_libro', views.ingresar_libro, name='ingresar_libro'), #lista de libros 
    path('registro_usuario', views.ingresar_usuario, name='registro_usuario'), #lista de libros 
]

