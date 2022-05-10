from django.shortcuts import render,HttpResponse

from indexapp.models import Producto,ImagenProducto
# Create your views here.

def index(request):
    productos=Producto.objects.all().filter(estado='5')
    imagenesP=ImagenProducto.objects.all()
    return render(request,"indexapp/index.html",{"productos": productos,"imagenes":imagenesP})