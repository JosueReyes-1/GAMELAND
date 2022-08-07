from django.contrib import admin

from shopping_cart.models import Lista_Productos, Estado_ListaP,Direccion
# Register your models here.

admin.site.register(Lista_Productos)
admin.site.register(Estado_ListaP)
admin.site.register(Direccion)

