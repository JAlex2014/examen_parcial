from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Usuario

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraseña')
        usuarioInfo = authenticate (
            request, username = nombreUsuario, password = contraUsuario)
        if usuarioInfo is not None:
            login(request, usuarioInfo)
            return HttpResponseRedirect(reverse('gestion_tienda:consolaUsuario'))
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index'))   
    return render(request, 'ingresoUsuario.html')

@login_required(login_url = 'http://127.0.0.1:8000')
def consolaUsuario(request):
    return render(request,'consolaUsuario.html')

@login_required(login_url = 'http://127.0.0.1:8000')
def gestionUsuarios(request):
    if request.method == 'POST':
        usernameUsuario = request.POST.get('usernameUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        rolUsuario = request.POST.get('rolUsuario')
        emailUsuario = request.POST.get('emailUsuario')
        celUsuario = request.POST.get('celUsuario')
        usuarioNuevo = User.objects.create(
            username = usernameUsuario,
            email = emailUsuario)
        usuarioNuevo.set_password(contraUsuario)
        usuarioNuevo.first_name = nombreUsuario
        usuarioNuevo.last_name = apellidoUsuario
        usuarioNuevo.is_staff = True
        usuarioNuevo.save()
        Usuario.objects.create(
            user = usuarioNuevo,
            Rol_del_usuario = rolUsuario,
            Nro_de_celular = celUsuario,
        )
        return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuarios'))
    return render(request,'gestionUsuarios.html', {
        'usuariosTotales': User.objects.all().order_by('id')
    })

def eliminarUsuario(request,ind):
    usuarioEliminar = User.objects.get(id=ind)
    Usuario.objects.get(user = usuarioEliminar).delete()
    usuarioEliminar.delete()
    return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuarios'))
    
@login_required(login_url = 'http://127.0.0.1:8000')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tienda:index'))