
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

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    fecha_fabricacion=models.DateField()
    marca=models.ForeignKey(Marca_Producto,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE)
#     # imagen=models.ImageField(update_to="productos", null=True)

class ImagenProducto(models.Model):
    imagen=models.ImageField(upload_to="img/productos")
    Producto=models.ForeignKey(Producto, on_delete=models.CASCADE)

