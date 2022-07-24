import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import  redirect, render
from django.contrib import messages
from requests import request

from shopping_cart.models import Lista_Productos
from indexapp.models import Producto



# Create your views here.
def view_products(request):
    user=request.user.id
    productos=Lista_Productos.objects.filter(user_id=user,estado_id=1)
    countP=productos.count()
    total=0
    

    
    for precio in productos:
        total=(total+precio.producto.precio)*precio.cantidad
        

    context={
        "listaproductos":productos,
        "totalpagar":total,
        "user1":user,
        "countP":countP,
    }
    return render(request,'shopping_cart/carrito_compras.html',context)


def add_cart(request):
    if request.method=="POST":
        product_pk=request.POST.get('product_pk')
        user_pk=request.user.id
        estado_pk=1
        cantidad=1
        producto=Lista_Productos.objects.filter(producto_id=product_pk , user_id=user_pk,estado_id=1) 
        
        print(producto)
        
        if user_pk is None:
            return render(request,'shopping_cart/carrito_compras.html')
        else:
            if producto.exists():
                for produ in producto:
                    Lista_Productos.objects.filter(producto_id=product_pk).update(cantidad=produ.cantidad+1)
                    messages.add_message(request=request,level=messages.SUCCESS, message="EL PRODUCTO SE AGREGO AL CARRITO")
                    return redirect('detalles',produ.producto.slug)
            else:
                Lista_Productos(producto_id=product_pk,cantidad=cantidad,user_id=user_pk,estado_id=estado_pk).save()
                messages.add_message(request=request,level=messages.SUCCESS, message="EL PRODUCTO SE AGREGO AL CARRITO")
            for produ in producto:
                return redirect('detalles',produ.producto.slug)
        
        

def delete_product(request):
    if request.method=="POST":
        product_pk=request.POST.get('product_pk')
        user_pk=request.user.id
        Lista_Productos.objects.get(producto_id=product_pk,user_id=user_pk,estado_id=1).delete()
        messages.add_message(request=request,level=messages.SUCCESS, message="EL PRODUCTO SE ELIMINO CORRECTAMENTE")
        return redirect('shopping_cart')

def payment_complete(request):
    user=request.user.id
    lista=Lista_Productos.objects.filter(user_id=user,estado_id=1)

    for producto in lista:
        cantidad=producto.cantidad
        stock=producto.producto.stock
        Producto.objects.filter(id=producto.producto.id).update(stock=stock-cantidad)
        

    lista.update(estado_id=2)
    
    return redirect('shopping_cart')
