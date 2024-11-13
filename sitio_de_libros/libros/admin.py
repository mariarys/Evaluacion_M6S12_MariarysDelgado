from django.contrib import admin
from .models import Book  

class BookAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'valoracion', 'fecha_creacion', 'fecha_modificacion')

admin.site.register(Book, BookAdmin)

