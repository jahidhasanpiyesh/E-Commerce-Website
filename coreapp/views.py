from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def user_login(request):
    return render(request, 'home/user_login.html')

def user_register(request):
    return render(request, 'home/user_register.html')