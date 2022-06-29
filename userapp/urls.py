from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LoginView
from userapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',LoginView.as_view(template_name="userapp/login.html"), name='login'),
    path('register',views.register, name='register')
]  