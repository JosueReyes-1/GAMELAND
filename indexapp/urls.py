from django.urls import path

from indexapp import views

urlpatterns = [
    
    path('',views.index,name="index"),
]
