from django.contrib import admin
from Gestion_WOP.models import *

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    fields = ( 'image_tag','TPimagen','Descripcion','Imagen',)
    readonly_fields = ('image_tag',)
    list_display = ('image_tag','Descripcion','TPimagen','Imagen',)
    search_fields = ['Descripcion']
    list_filter = ('TPimagen',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('User', 'Telefono', 'Regiones', 'Nivel', 'Puntaje')
    search_fields = [ 'Telefono', 'User', 'Puntaje']
    list_filter = ('Regiones', 'Nivel',)

class MensajesAdmin(admin.ModelAdmin):
    list_display = ('clientees', 'tmensajees', 'Asunto', 'Mensaje')
    search_fields = ['Asunto', 'Mensaje']
    list_filter = ('tmensajees',)

class NivelusuarioAdmin(admin.ModelAdmin):
    list_display = ('Elo_Usuario', 'Puntaje_minimo')
    search_fields = ['Elo_Usuario', 'Puntaje_minimo']

class Admin_PaginaAdmin(admin.ModelAdmin):
    list_display = ('UserAdmin', 'AliasAdmin', 'EmailAdmin')
    search_fields = ['UserAdmin', 'AliasAdmin', 'EmailAdmin']

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('Titular', 'Autor', 'Cuerpo', 'Imagen', 'Link_YT', 'Fecha_noticia')
    search_fields = ['Titular', 'Autor']
    list_filter = ('Autor',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('Usuariocom', 'Noticiacom', 'Comentariocom', 'Fecha_comentario')
    search_fields = ['Usuariocom', 'Noticiacom']
    list_filter = ('Usuariocom', 'Noticiacom',)

admin.site.register(Galeria, ImageAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Mensajes, MensajesAdmin)
admin.site.register(Tipo_Mensaje)
admin.site.register(Tipo_img)
admin.site.register(Region)
admin.site.register(Nivel_Usuario, NivelusuarioAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Comentarios_Noti, ComentarioAdmin)
admin.site.register(Admin_Pagina, Admin_PaginaAdmin)






