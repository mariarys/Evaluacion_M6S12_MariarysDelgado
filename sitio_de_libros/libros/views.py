from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Book
from .forms import BookForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'libros/index.html'

@login_required
def lista_libro(request):
    books = Book.objects.all()
    libro_filtrado = Book.objects.filter(valoracion__gt=1500)
    
    return render(request, 'libros/lista_libros.html', {
        'books': books,          # Libros completos
        'libro_filtrado': libro_filtrado  # Libros filtrados
    })

@login_required
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # autentica el usuario en la db
        if user is not None: # si existe
            login(request, user) # persistir la sesión del usuario
            return redirect('index') # redireccionar a ruta seeleccionada
        else:
            messages.error(request, 'Credenciales inválidas')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'libros/login.html')  



