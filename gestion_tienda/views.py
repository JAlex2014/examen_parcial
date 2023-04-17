from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Usuario, producto

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
    if request.user.usuario.Rol_del_usuario == 'Administrador':
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
    else:
        return HttpResponseRedirect(reverse('gestion_tienda:consolaUsuario'))

@login_required(login_url = 'http://127.0.0.1:8000')
def gestionProductos(request, ind):
    if request.method == 'POST':
        usuario = User.objects.get(id=ind)
        nameProducto = request.POST.get('nameProducto')
        codigoProducto = request.POST.get('codigoProducto')
        precioCompra = request.POST.get('precioCompra')
        precioVenta = request.POST.get('precioVenta')
        producto.objects.create(
            User = usuario,
            Nombre_del_producto = nameProducto,
            Codigo = codigoProducto,
            Precio_de_compra = precioCompra,
            Precio_de_venta = precioVenta,
        )
        return HttpResponseRedirect(reverse('gestion_tienda:gestionProductos', kwargs={'ind':ind}))
    usuarioInformacion = User.objects.get(id=ind)
    productosTotales = producto.objects.all()
    return render(request, 'gestionProductos.html',{
        'usuarioInformacion' : usuarioInformacion,
        'productosTotales' : productosTotales
    })

@login_required(login_url = 'http://127.0.0.1:8000')
def eliminarUsuario(request,ind):
    if request.user.usuario.Rol_del_usuario == 'Administrador':
        usuarioEliminar = User.objects.get(id=ind)
        Usuario.objects.get(user = usuarioEliminar).delete()
        usuarioEliminar.delete()
        return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuarios'))
    else:
        return HttpResponseRedirect(reverse('gestion_tienda:consolaUsuario'))

@login_required(login_url = 'http://127.0.0.1:8000')
def eliminarProducto(request,idTarea, idUsuario):
    if request.user.usuario.Rol_del_usuario == 'Administrador':
        productoEliminar = producto.objects.get(Codigo = idTarea)
        productoEliminar.delete()
        return HttpResponseRedirect(reverse('gestion_tienda:gestionProductos', kwargs={'ind': idUsuario}))
    else:
        return HttpResponseRedirect(reverse('gestion_tienda:consolaUsuario'))
    
@login_required(login_url = 'http://127.0.0.1:8000')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tienda:index'))

