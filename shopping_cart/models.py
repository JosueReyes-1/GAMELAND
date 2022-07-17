from itertools import product
from math import prod
from statistics import mode
from django.db import models
import indexapp
from indexapp.models import Producto
from django.contrib.auth.models import User

class Estado_ListaP(models.Model):
    estado=models.CharField(max_length=10)

class Lista_Productos(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cantidad=models.IntegerField(null=True)
    estado=models.ForeignKey(Estado_ListaP,on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.nombre


# Create your models here.

