from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def user_login(request): 
    # if request.method == 'POST':
    #     fm = user_login(request=POST)
    return render(request, 'home/user_login.html')

def user_register(request):
    if request.method == 'POST':
        username= request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        
        # chack in password1 or password2 similar 
        if password == con_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect(user_register)
            
            elif User.objects.filter(email=email):
                messages.error(request, 'Email is already taken.')
                return redirect(user_register)
                  
            else:
                user_info=User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
                user_info.save()
                messages.success(request, 'Your Account Created Successfully !')
        else:
            messages.error(request, 'Pssword Not Match !!')
    return render(request, 'home/user_register.html')