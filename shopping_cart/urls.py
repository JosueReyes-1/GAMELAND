

from django.urls import path
from shopping_cart import views



urlpatterns = [
    path('productos/carrito/',views.add_cart),
    path('listaproductos/',views.view_products, name='lista'),
]