from queue import Empty
from django.shortcuts import render,HttpResponse
from indexapp.models import Producto,ImagenProducto,Estado
# Create your views here.

def index(request):
    # consulta de productos nuevos
    nuevo=Estado.objects.get(estado='nuevo')
    productos_nuevos=Producto.objects.filter(estado=nuevo)

    imagenesP=ImagenProducto.objects.all()

    # consulta de productos en descuentos
    desc=Estado.objects.get(estado='descuento')
    productos_desc=Producto.objects.filter(estado=desc)

    context={
        "nuevos": productos_nuevos,
        "desc": productos_desc,
        "imagenes":imagenesP,
    }
    return render(request,"indexapp/index.html", context)

def detalles(request, slug_text):
    producto=Producto.objects.filter(slug=slug_text)
    if producto.exists():
        producto=producto.first()
    else:
        return HttpResponse("<h5>Pagina No encontrada</h5>")
    
    context={
        'producto':producto
    }
    
    return render(request,'indexapp/detalles.html',context)