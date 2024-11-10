from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Book
from .forms import BookForm
from django.contrib import messages
from .forms import CustomUserCreationForm


class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'libros/index.html'

def lista_libro(request):
    books = Book.objects.all()
    libro_filtrado = Book.objects.filter(valoracion__gt=1500)
    
    return render(request, 'libros/lista_libros.html', {
        'books': books,          # Libros completos
        'libro_filtrado': libro_filtrado  # Libros filtrados
    })

def ingresar_libro(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡El libro se ha agregado exitosamente!")
            return redirect('lista_libros')  # Redirige a la lista de libros después de agregar
    else:
        form = BookForm()

    return render(request, 'libros/ingresar_libro.html', {'form': form})

def ingresar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡El usuario se ha agregado exitosamente!")
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'libros/registro_usuario.html', {'form': form})



