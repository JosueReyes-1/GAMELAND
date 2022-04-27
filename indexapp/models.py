
from django.db import models

# Create your models here.

class Marca_Producto(models.Model):
    nombre_marca=models.CharField(max_length=30)

class Categoria_Producto(models.Model):
    nombre_categ=models.CharField(max_length=30)

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    fecha_fabricacion=models.DateField()
    marca=models.ForeignKey(Marca_Producto,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE)
#     # imagen=models.ImageField(update_to="productos", null=True)

class ImagenProducto(models.Model):
    imagen=models.ImageField(upload_to="producto")
    Producto=models.ForeignKey(Producto, on_delete=models.CASCADE)

