from xml.dom.minidom import Document
from django.urls import path

from indexapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.index,name="index"),
    path('productos/<slug:slug_text>',views.detalles),
    path('categorias/<slug:slug_text>',views.categorias),
]  
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
