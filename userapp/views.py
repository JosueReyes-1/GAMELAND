import email
from email import message
from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# login
from django.contrib.auth import authenticate,login,logout

from .forms import CreateUserForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
    

    context={
        'form':form,
    }
    return render(request,"userapp/register.html",context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email=request.POST.get('email')
            password=request.POST.get('password')

            user=authenticate(request,username=email,password=password)
            print(email)
            if user is not None:
                login(request,user)
                return redirect ('/')
            else:
                messages.info(request,'el correo o la contrasena')
                
        
    
    context={

    }
    return render(request,"userapp/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('login')

