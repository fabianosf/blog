from ast import AugStore
from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User



class Post(models.Model):
    titulo_post = models.CharField('Titulo', max_length=255)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_post = models.DateTimeField('Data', auto_now_add=True)
    conteudo_post = models.TextField('Conteudo')
    excerto_post = models.TextField('Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField('Publicado ?',default=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo_post
