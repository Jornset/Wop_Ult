from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def post_list(request):
    user = request.user
    if user.has_perm('Gestion_WOP.AdminGen'):
        return render (request, 'http://127.0.0.1:8000/admin/', {'posts':posts})
    else:
        return render (request, 'Gestion_WOP/Proyectos.html')

def WOP_CORP(request):

    Noticiases = Noticia.objects.all()

    return render(request, 'Gestion_WOP/WOP_CORP.html', {
        'Noticiases':Noticiases
    })


def WOP_Origins(request):
    return render(request, 'Gestion_WOP/WOP_Origins.html')


def Staff(request):
    return render(request, 'Gestion_WOP/Staff.html')


def Proyectos(request):
    return render(request, 'Gestion_WOP/Proyectos.html')


def Noticias(request):

    Noticiases = Noticia.objects.all()

    return render(request, 'Gestion_WOP/Noticias.html', {
        'Noticiases':Noticiases
    })


def Mensaje(request):
    return render(request, 'Gestion_WOP/Mensaje.html')


def GOLDENWATCH(request):
    return render(request, 'Gestion_WOP/GOLDENWATCH.html')


def Contacto(request):
    
    Comentario = Mensajes.objects.all()
    tipo_mensaje = Tipo_Mensaje.objects.all()
    region = Region.objects.all()

    if request.POST:
        lemensaje = Mensajes()
        lemensaje.clientees = request.POST.get('Nombre')
        lemensaje.emailmensaje = request.POST.get('Email')
        lemensaje.Telefonomensaje = request.POST.get('Telefono')

        leRegion = Region()
        leRegion.id =request.POST.get('Ciudad') 
        lemensaje.RegionMensaje = leRegion

        leTipoMensaje = Tipo_Mensaje()
        leTipoMensaje.id =request.POST.get('Tipo_mensaje')
        lemensaje.tmensajees = leTipoMensaje 

        lemensaje.Asunto = request.POST.get('Asunto')
        lemensaje.Mensaje = request.POST.get('Mensaje')

        lemensaje.save()


    return render(request, 'Gestion_WOP/Contacto.html', {
        'Comentario':Comentario, 'tipo_mensaje': tipo_mensaje, 'region': region
    })


def welcome(request):
        if request.user.is_authenticated:
            return render(request, "Gestion_WOP/welcome.html")
        return redirect('/login')

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "Gestion_WOP/register.html", {'form': form})

def login(request):
            # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "Gestion_WOP/login.html", {'form': form})

def logout(request):
    # Redireccionamos a la portada
    do_logout(request)
    return redirect('/')

def password_reset(request):
    return render(request, 'Registration/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'Registration/password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'Registration/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request, 'Registration/password_reset_complete.html')

def CRUD_noticias(request):
    Admin_Paginas = Admin_Pagina.objects.all()
    Noticiases = Noticia.objects.all()

    if request.POST:
        lenoticia = Noticia()

        lenoticia.Titular = request.POST.get('Titular')
        
        leAdmin_Pagina = Admin_Pagina()
        leAdmin_Pagina.UserAdmin =request.POST.get('Autor') 
        lenoticia.Autor = leAdmin_Pagina

        lenoticia.Cuerpo = request.POST.get('Cuerpo')
        lenoticia.Imagen = request.FILES.get('Imagen')
        lenoticia.Link_YT = request.POST.get('LinkYT')
        lenoticia.Fecha_noticia = request.POST.get('FechaPublicacion')

        lenoticia.save()

    return render(request, 'Gestion_WOP/CRUD_noticias.html', {
        'Noticiases':Noticiases, 'Admin_Paginas':Admin_Paginas
    })

def Eliminar_Noticia(request, id):

    eliNoticia = Noticia.objects.get(id=id)

    eliNoticia.delete()

    return redirect('CRUD_noticias')

def Modificar_Noticia(request, id):

    modiNoticia = Noticia.objects.get(id=id)
    modiAdmin_Paginas = Admin_Pagina.objects.all()

    variables = {
        'modiNoticia':modiNoticia,
        'modiAdmin_Paginas':modiAdmin_Paginas
    }

    if request.POST:
        lenoticia = Noticia()

        lenoticia.id = request.POST.get('txtid')

        lenoticia.Titular = request.POST.get('Titular')
        
        leAdmin_Pagina = Admin_Pagina()
        leAdmin_Pagina.UserAdmin =request.POST.get('Autor') 
        lenoticia.Autor = leAdmin_Pagina

        lenoticia.Cuerpo = request.POST.get('Cuerpo')
        lenoticia.Imagen = request.FILES.get('Imagen')
        lenoticia.Link_YT = request.POST.get('LinkYT')
        lenoticia.Fecha_noticia = request.POST.get('FechaPublicacion')

        lenoticia.save()
        return redirect('CRUD_noticias')

    return render(request, 'Gestion_WOP/modificar_noticia.html', variables)
