from django.shortcuts import render,render
from django.contrib.auth import authenticate

# Create your views here.
def home(requist):


    return render(requist, 'home.html')


def login(requist):
    return render(requist, 'login.html')