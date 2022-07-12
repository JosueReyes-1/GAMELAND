from unicodedata import name
from django.urls import include, path
from django.contrib.auth.views import LoginView
from userapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    
    path('accounts/',include('allauth.urls')),
]  