from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', WOP_CORP, name="WOP_CORP"),
    path('WOP_Origins/', WOP_Origins, name="WOP_Origins"),
    path('Staff/', Staff, name="Staff"),
    path('Proyectos/', Proyectos, name="Proyectos"),
    path('Noticias/', Noticias, name="Noticias"),
    path('Contacto/Mensaje/', Mensaje, name="Mensaje"),
    path('GOLDENWATCH/', GOLDENWATCH, name="GOLDENWATCH"),
    path('Contacto/', Contacto, name="Contacto"),
    path('register/', register, name='Register'),
    path('login/', login, name='Login'),
    path('logout/', logout, name='Logout'),
    path('password_reset', password_reset,name='password_reset'),
    path('password_reset_done/', password_reset_done, name='password_reset_done'),
    path('password_reset_confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete/', password_reset_complete, name='password_reset_complete'),
    path('CRUD_noticias/', CRUD_noticias, name='CRUD_noticias'),
    path('Eliminar_Noticia/<id>/', Eliminar_Noticia, name='Eliminar_Noticia'),
    path('Modificar_Noticia/<id>/', Modificar_Noticia, name='Modificar_Noticia'),


]