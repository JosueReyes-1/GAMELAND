from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request,"userapp/login.html")

def register(request):

    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
    user.save()
    return render(request,"userapp/login.html")