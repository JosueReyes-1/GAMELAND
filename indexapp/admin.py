from django.contrib import admin


from indexapp.models import Marca_Producto,Categoria_Producto,Producto, ImagenProducto
# Register your models here.

class ImagenProductoAdmin(admin.TabularInline):
    model=ImagenProducto

class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre","precio","marca"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_per_page=10
    inlines=[
        ImagenProductoAdmin
    ]


admin.site.register(Marca_Producto)
admin.site.register(Categoria_Producto)
admin.site.register(Producto, ProductoAdmin)
