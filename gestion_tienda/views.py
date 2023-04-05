from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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