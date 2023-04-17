from django.db import models
from django.contrib.auth.models import User
from datetime import date
from djmoney.models.fields import MoneyField

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    Nombre = models.CharField(max_length = 32, default = 'Usuario') 
    Apellido = models.CharField(max_length = 32, default = 'Apellido') 
    Email = models.EmailField(max_length = 254)
   #Username
   #Contraseña 
    Rol_del_usuario = models.CharField(max_length = 32, default = 'Vendedor')
    Nro_de_celular = models.CharField(max_length = 32, default = '999999999')
    Fecha_de_ingreso = models.DateField(default = date.today)

class producto(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Nombre_del_producto = models.CharField(max_length = 32)
    Codigo = models.CharField(max_length = 32)
    Precio_de_compra = MoneyField(decimal_places=2,default=0,default_currency='PEN',max_digits=8)
    Precio_de_venta= MoneyField(decimal_places=2,default=0,default_currency='PEN',max_digits=8)