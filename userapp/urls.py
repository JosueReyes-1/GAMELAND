from django.urls import path

from userapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',views.login),
]  