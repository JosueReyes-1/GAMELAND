import email
from email import message
from multiprocessing import context
from queue import Empty
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



