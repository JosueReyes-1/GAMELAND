
from django.shortcuts import redirect, render,HttpResponse
from django.http import JsonResponse
from indexapp.models import Producto,ImagenProducto
from shopping_cart.models import Lista_Productos
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.models import User


def index(request):
    # consulta de productos nuevos
    productos_nuevos=Producto.objects.filter(estado__estado='nuevo',stock__gte=1)
    imagenesP=ImagenProducto.objects.all()
    # consulta de productos en descuentos
    productos_desc=Producto.objects.filter(estado__estado='descuento',stock__gte=1)

    context={
        "nuevos": productos_nuevos,
        "desc": productos_desc,
        "imagenes":imagenesP,
    }
    return render(request,"indexapp/index.html", context)


def detalles(request, slug_text):
    productos=Producto.objects.filter(slug=slug_text,stock__gte=1)
    imagenesP=ImagenProducto.objects.filter(producto__slug=slug_text) 
    if productos.exists() and imagenesP.exists():
        productos=productos.first()
    else:
        return redirect('index')
    
    context={
        'producto':productos,
        'imagenes':imagenesP,
    }
    
    return render(request,'indexapp/detalles.html',context)


def categorias(request, slug_text):
    
    productos=Producto.objects.filter(categoria__slug=slug_text)
    imagenesP=ImagenProducto.objects.all()
    
    p=Paginator(productos,10)
    page_num=request.GET.get('page',1)

    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)


    context={
        'productos':page,
        'imagenes':imagenesP,

    }
    
    return render(request,'indexapp/lista_productos.html',context)

