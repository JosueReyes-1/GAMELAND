from queue import Empty
from django.shortcuts import render,HttpResponse
from indexapp.models import Producto,ImagenProducto,Estado
# Create your views here.

def index(request):
    # consulta de productos nuevos
    productos_nuevos=Producto.objects.filter(estado__estado='nuevo')
    imagenesP=ImagenProducto.objects.all()
    # consulta de productos en descuentos
    productos_desc=Producto.objects.filter(estado__estado='descuento')

    context={
        "nuevos": productos_nuevos,
        "desc": productos_desc,
        "imagenes":imagenesP,
    }
    return render(request,"indexapp/index.html", context)



def detalles(request, slug_text):
    productos=Producto.objects.filter(slug=slug_text)
    imagenesP=ImagenProducto.objects.filter(producto__slug=slug_text) 

    if productos.exists():
        productos=productos.first()
    else:
        return HttpResponse("<h5>Pagina No encontrada</h5>")
    
    context={
        'producto':productos,
        'imagenes':imagenesP,
    }
    
    return render(request,'indexapp/detalles.html',context)