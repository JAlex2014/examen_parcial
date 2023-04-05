from django.urls import path
from . import views

app_name = 'gestion_tienda'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('consolaUsuario', views.consolaUsuario, name = 'consolaUsuario')
]