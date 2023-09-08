from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, blank=False, null=False)
    estado = models.BooleanField('Categoria Activada/Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now_add=True, auto_now=False)

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.nombre

class Autor(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombres del Autor', max_length=255, blank=False, null=False)
    apellidos = models.CharField('Apellidos del Autor', max_length=255, blank=False, null=False)
    facebook = models.URLField('FaceBook', blank=True, null=True)
    twitter = models.URLField('Twitter', blank=True, null=True)
    instagram = models.URLField('Instagram', blank=True, null=True)
    web = models.URLField('Web', blank=True, null=True)
    email = models.EmailField('Correo Electronico', blank=False, null=False)
    estado = models.BooleanField('Autor Activado/Desactivado', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now_add=True, auto_now=False)

    class Meta():
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellidos}'

class Post(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha Creacion', auto_now_add=True, auto_now=False)

    class Meta:
    
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self) -> str:
        return self.titulo