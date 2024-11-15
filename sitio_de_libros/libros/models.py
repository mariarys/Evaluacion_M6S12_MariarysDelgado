from django.db import models

class Book(models.Model):
    # Atributos
    titulo = models.CharField(max_length=100, null=False)
    autor = models.CharField(max_length=50, null=False)
    valoracion = models.IntegerField(help_text='Valoración entre 0 y 100')
    
    # Nuevos campos de fecha
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    fecha_modificacion = models.DateTimeField(auto_now=True)  # Fecha de modificación

    # Metadatos
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        permissions = [
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Owner"),
        ]

    def __str__(self):
        return self.titulo  
