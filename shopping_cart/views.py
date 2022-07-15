from django.http import HttpResponse
from django.shortcuts import redirect, render
from indexapp.models import Producto

from shopping_cart.models import Lista_Productos


# Create your views here.
def view_products(request):
    # user_pk=request.POST.get('user_pk')
    # productos=Lista_Productos.objects.filter(user_id=user_pk)

    context={
        # "productos":productos,
    }
    return render(request,'shopping_cart/carrito_compras.html',context)


def add_cart(request):
    product_pk=request.POST.get('product_pk')
    user_pk=request.POST.get('user_pk')
    estado_pk=1

    producto=Lista_Productos.objects.filter(producto_id=product_pk)

    if producto.exists():
        return HttpResponse('hola no se pudo')
    else:
        Lista_Productos(producto_id=product_pk,user_id=user_pk,estado_id=estado_pk).save()
    return HttpResponse(producto)
    