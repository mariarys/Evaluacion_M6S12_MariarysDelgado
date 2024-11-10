# models.py
from django.db import models

class Book(models.Model):
    # Atributos
    titulo = models.CharField(max_length=100, null=False)
    autor = models.CharField(max_length=50, null=False)
    valoracion = models.IntegerField(help_text='Valoración entre 0 y 100')

    def __str__(self):
        return f"{self.titulo} - {self.autor} (Valoración: {self.valoracion})"
