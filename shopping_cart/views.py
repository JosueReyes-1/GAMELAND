from django.http import HttpResponse
from django.shortcuts import  redirect, render

from shopping_cart.models import Lista_Productos
from indexapp.models import Producto



# Create your views here.
def view_products(request):
    user=request.user.id
    productos=Lista_Productos.objects.filter(user_id=user)
    countP=productos.count()
    total=0

    for precio in productos:
        total=total+precio.producto.precio


    context={
        "listaproductos":productos,
        "totalpagar":total,
        "countP":countP,
    }
    return render(request,'shopping_cart/carrito_compras.html',context)


def add_cart(request):
    if request.method=="POST":
        product_pk=request.POST.get('product_pk')
        user_pk=request.user.id
        estado_pk=1
        cantidad=1
        producto=Lista_Productos.objects.filter(producto_id=product_pk)

        print(producto)
        
        if user_pk is None:
            return render(request,'shopping_cart/carrito_compras.html')
        else:
            for produ in producto:
                if producto.exists():
                    
                        Lista_Productos.objects.filter(producto_id=product_pk).update(cantidad=produ.cantidad+1)
                        return redirect('detalles',produ.producto.slug)
                else:
                    Lista_Productos(producto_id=product_pk,cantidad=cantidad,user_id=user_pk,estado_id=estado_pk).save()
                return redirect('detalles',produ.producto.slug)
        
        

def delete_product(requets):
    if requets.method=="POST":
        product_pk=requets.POST.get('product_pk')
        print(product_pk)
        Lista_Productos.objects.get(producto_id=product_pk).delete()
        return redirect('shopping_cart')