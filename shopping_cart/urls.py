

from django.urls import path
from shopping_cart import views



urlpatterns = [
    path('productos/carrito/',views.add_cart),
    path('listaproductos/',views.view_products, name='shopping_cart'),
    path('deleteproducto/',views.delete_product,name='eliminar'),
    path('complete/',views.payment_complete,name='complete'),

    path('direciones/',views.create_direction,name='direciones'),
    path('borrardireccion/',views.delete_direction,name='delete_direction'),
    path('cambiardireccion/',views.change_direction,name='change_direction')
]