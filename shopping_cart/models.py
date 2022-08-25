

from re import T
from statistics import mode
from xmlrpc.client import boolean
from django.db import models
import indexapp
from indexapp.models import Producto
from django.contrib.auth.models import User

class Estado_ListaP(models.Model):
    estado=models.CharField(max_length=10)

class Direccion(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pais=models.CharField(max_length=20)
    ciudad=models.CharField(max_length=20)
    nombre=models.CharField(max_length=30)
    num_exterior=models.CharField(max_length=20)
    num_tel=models.IntegerField()
    domicilio=models.CharField(max_length=255)
    cp=models.IntegerField()
    instrucciones=models.CharField(max_length=300)
    estado=models.BooleanField(null=True)
    


class Lista_Productos(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cantidad=models.IntegerField(null=True)
    estado=models.ForeignKey(Estado_ListaP,on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.nombre


class Ticket(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    direccion=models.ForeignKey(Direccion,on_delete=models.PROTECT)
    productos=models.ForeignKey(Lista_Productos,on_delete=models.PROTECT)
    # fecha=models.DateField()


# Create your models here.

