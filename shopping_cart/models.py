from itertools import product
from math import prod
from pyexpat import model
from statistics import mode

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
    domicio=models.CharField(max_length=255)
    cp=models.IntegerField()
    intrucciones=models.CharField(max_length=300)
    
class Ticket(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    direccion=models.ForeignKey(Direccion,on_delete=models.PROTECT)
    fecha=models.DateField()

class Lista_Productos(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cantidad=models.IntegerField(null=True)
    estado=models.ForeignKey(Estado_ListaP,on_delete=models.CASCADE)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.producto.nombre





# Create your models here.

