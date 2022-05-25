
from turtle import ondrag
from django.db import models
from django.db.models.signals import pre_save
from gameland.utils import unique_slug_generator
# Create your models here.

class Marca_Producto(models.Model):
    nombre_marca=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_marca

class Categoria_Producto(models.Model):
    nombre=models.CharField(max_length=30)
    imagen=models.ImageField(null=True)
    slug=models.SlugField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.nombre

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
    slug=models.SlugField(max_length=200, null=True, blank=True)

# slug
def slug_generator(sender,instance, *args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Producto)
pre_save.connect(slug_generator, sender=Categoria_Producto)

class ImagenProducto(models.Model):
    imagen=models.ImageField(upload_to='productos',null=True)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="imagenes")

    
