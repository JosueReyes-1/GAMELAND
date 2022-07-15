

from django.urls import path
from shopping_cart import views



urlpatterns = [
    path('productos/carrito/',views.add_cart),
    path('carrito/',views.view_products, name='carrito'),
]