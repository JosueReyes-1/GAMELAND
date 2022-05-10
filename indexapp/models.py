
from turtle import ondrag
from django.db import models

# Create your models here.

class Marca_Producto(models.Model):
    nombre_marca=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_marca

class Categoria_Producto(models.Model):
    nombre_categ=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_categ

class Estado(models.Model):
    estado=models.CharField(max_length=30)

    def __str__(self):
        return self.estado


class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    fecha_fabricacion=models.DateField()
    stock=models.IntegerField(default=1)
    marca=models.ForeignKey(Marca_Producto,on_delete=models.CASCADE)
    categoria=models.ManyToManyField(Categoria_Producto)
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE)

class ImagenProducto(models.Model):
    imagen=models.ImageField(upload_to='productos',null=True)
    Producto=models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="imagenes")

