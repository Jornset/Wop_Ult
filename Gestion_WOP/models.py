import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from datetime import datetime
from django.utils.translation import ugettext as _

# Create your models here.

class Tipo_img (models.Model):
    Timagen = models.CharField(max_length=35, unique=True)

    def Timagencom (self):
        TimagenRes = "{0}"
        return TimagenRes.format(self.Timagen)

    def __str__(self):
        return self.Timagencom()

    class Meta:
        verbose_name = "Tipo de Imagen"
        verbose_name_plural = "Tipo de Imagenes"


class Galeria (models.Model):
    TPimagen = models.ForeignKey(Tipo_img, on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=30)
    Imagen = models.ImageField(upload_to='Galeria', null=True)

    def Galeriacom (self):
        GaleriaRes = "{0} -- {1}"
        return GaleriaRes.format(self.Descripcion, self.Imagen)

    def __str__(self):
        return self.Galeriacom()

    def url(self):
        return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.Imagen)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="350" height="150" />'.format(self.url()) )
        image_tag.short_description = 'Galeria'    

    def __unicode__(self):
        # add __str__() if using Python 3.x
        return self.Descripcion
    
    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galeria"


class Nivel_Usuario (models.Model):
    Elo_Usuario = models.CharField(max_length=40, unique=True)
    Puntaje_minimo = models.PositiveSmallIntegerField()

    def NUsuariocom (self):
        NUsuarioRes = "{0} -- {1}"
        return NUsuarioRes.format(self.Elo_Usuario, self.Puntaje_minimo)

    def __str__(self):
        return self.NUsuariocom()

    class Meta:
        verbose_name = "Nivel de Usuario"
        verbose_name_plural = "Nivel de Usuarios"

class Tipo_Mensaje (models.Model):
    Descripcion = models.CharField(max_length=35)

    def Tmensajecom (self):
        TmensajeRes = "{0}"
        return TmensajeRes.format(self.Descripcion)

    def __str__(self):
        return self.Tmensajecom()

    class Meta:
        verbose_name = "Tipo de mensaje"
        verbose_name_plural = "Tipos de mensajes"


class Region (models.Model):
    NomRegion = models.CharField(max_length=50, unique=True)

    def Regioncom (self):
        RegionRes = "{0}"
        return RegionRes.format(self.NomRegion)

    def __str__(self):
        return self.Regioncom()

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"


class Cliente (models.Model):
    User = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Telefono = models.PositiveSmallIntegerField()
    Regiones = models.ForeignKey(Region, on_delete=models.CASCADE)
    Nivel = models.ForeignKey(Nivel_Usuario, on_delete=models.CASCADE)
    Puntaje = models.PositiveSmallIntegerField()

    def NombreCompleto (self):
        NombreResumen = "{0}"
        return NombreResumen.format(self.User)

    def __str__(self):
        return self.NombreCompleto()
    
    class Meta:
        permissions = (
            ('AdminGen',_('Es administrador General')),
            ('AdminPag',_('Es administrador de la pagina')),
        )

class Mensajes (models.Model):
    clientees = models.CharField(max_length=150)
    emailmensaje = models.EmailField()
    Telefonomensaje = models.PositiveSmallIntegerField()
    RegionMensaje = models.ForeignKey(Region, on_delete=models.CASCADE)
    tmensajees = models.ForeignKey(Tipo_Mensaje, on_delete=models.CASCADE)
    Asunto = models.CharField(max_length=30)
    Mensaje = models.CharField(max_length=1000)

    def MensajeCompleto (self):
        MensajesResumen = "{0} -- {1}"
        return MensajesResumen.format(self.clientees, self.Asunto)

    def __str__(self):
        return self.MensajeCompleto()

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"


class Admin_Pagina (models.Model):
    UserAdmin = models.CharField(max_length=50 , unique=True)
    PasswordAdmin = models.CharField(max_length=50)
    AliasAdmin = models.CharField(max_length=50)
    EmailAdmin = models.EmailField()

    def Admin_PaginaCompleto (self):
        Admin_PaginaResumen = "{0} -- {1}"
        return Admin_PaginaResumen.format(self.UserAdmin, self.AliasAdmin)

    def __str__(self):
        return self.Admin_PaginaCompleto()

    class Meta:
        verbose_name = "Admin_Pagina"
        verbose_name_plural = "Admin_Paginas"

class Noticia (models.Model):
    Titular = models.CharField(max_length=200)
    Autor = models.CharField(max_length=50)
    Cuerpo = models.CharField(max_length=10500)
    Imagen = models.ImageField(upload_to='Noticias', null=True, blank=True)
    Link_YT = models.CharField(max_length=400, null=True, blank=True)
    Fecha_noticia = models.DateTimeField()


    def NoticiaCompleto (self):
        NoticiaResumen = "{0} -- {1}"
        return NoticiaResumen.format(self.Autor, self.Titular)

    def __str__(self):
        return self.NoticiaCompleto()
    
    def Formato_fecha (Fecha_noticia):
        messsage = "{} de {} del {}"
        return Formato_fecha.format(day, month, year)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"


class Comentarios_Noti (models.Model):
    Usuariocom = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Noticiacom = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    Comentariocom = models.CharField(max_length=1500)
    Fecha_comentario = models.DateTimeField()


    def ComentarioCompleto (self):
        ComentarioResumen = "{0} -- {1}"
        return ComentarioResumen.format(self.Usuariocom, self.Fecha_comentario)

    def __str__(self):
        return self.ComentarioCompleto()

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"