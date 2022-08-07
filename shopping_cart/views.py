import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import  redirect, render
from django.contrib import messages
from requests import request

from shopping_cart.models import Direccion, Lista_Productos
from indexapp.models import Producto



# Create your views here.
def view_products(request):
    user=request.user.id
    productos=Lista_Productos.objects.filter(user_id=user,estado_id=1)
    countP=productos.count()
    total=0
    

    direccionPrincipal=Direccion.objects.filter(user_id=user,estado=True)
    direciones=Direccion.objects.filter(user_id=user)
    for precio in productos:
        total=(total+precio.producto.precio)*precio.cantidad
        

    context={
        "direcciones":direciones,
        "direccionesP":direccionPrincipal,
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


def create_direction(request):
    if request.method=='POST':
        user=request.user.id
        name=request.POST.get('txtname')
        pais=request.POST.get('txtpais')
        ciudad=request.POST.get('txtciudad')
        direccion=request.POST.get('txtdireccion')
        cp=request.POST.get('txtcp')
        num_ext=request.POST.get('txtnum_ex')
        tel=request.POST.get('txttel')
        instrucciones=request.POST.get('txtinstrucciones')
        Direccion.objects.filter(user_id=user,estado=True).update(estado=False)
        Direccion(user_id=user,pais=pais,ciudad=ciudad,nombre=name,num_exterior=num_ext,domicilio=direccion,cp=cp,instrucciones=instrucciones,num_tel=tel,estado=True).save()


    
   
    context={
        
    }
    return render(request,'shopping_cart/form_direcciones.html',context)


def delete_direction(request):
    if request.method=='POST':
        user=request.user.id
        direccion_id=request.POST.get('direccion_id')
        direccionv=Direccion.objects.get(user_id=user,pk=direccion_id)

        if direccionv.estado==True:
            print('hola')
        else:
            Direccion.objects.get(pk=direccion_id,user_id=user).delete()

    return redirect('shopping_cart')

def change_direction(request):
    user=request.user.id
    direccion_id=request.POST.get('direccion_id')

    Direccion.objects.filter(user_id=user).update(estado=False)
    
    Direccion.objects.filter(user_id=user,pk=direccion_id).update(estado=True)
    return redirect('shopping_cart')