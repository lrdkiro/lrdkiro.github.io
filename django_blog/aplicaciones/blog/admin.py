from django.contrib import admin
from .models import*
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Configurando los botones import/export
class CategoriaResource(resources.ModelResource):
    
    class Meta:

        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Activa la barra de busqueda en el panel de admin para Categoria
    search_fields = ['nombre']
    # Edita como se ven los nombres de las propiedades en el panel de admin
    list_display = ('nombre', 'estado','fecha_creacion',)
    # Annadir los botones de import/export
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    
    class Meta:

        model = Categoria

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ['nombre', 'apellidos', 'email']
    list_display = ('nombre', 'apellidos', 'email', 'estado', 'fecha_creacion',)
    resource_class = AutorResource


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)