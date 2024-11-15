from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valoracion', 'fecha_creacion', 'fecha_modificacion', 'rating') 

    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

    list_filter = ('valoracion', 'fecha_modificacion')

    def rating(self, obj):
        if obj.valoracion < 1000:
            return "Baja"
        elif 1000 <= obj.valoracion <= 2500:
            return "Media"
        else:
            return "Alta"
    
    rating.short_description = 'Rating'
    rating.admin_order_field = 'valoracion'  

admin.site.register(Book, BookAdmin)

