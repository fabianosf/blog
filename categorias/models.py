from tabnanny import verbose
from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField('Nome:', max_length=50)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome_categoria
