from django.urls import path
from . import views

app_name = 'gestion_tienda'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('consolaUsuario', views.consolaUsuario, name = 'consolaUsuario'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
    path('gestionUsuarios', views.gestionUsuarios, name='gestionUsuarios'),
    path('eliminarUsuario/<str:ind>', views.eliminarUsuario, name='eliminarUsuario')
]