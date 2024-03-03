from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                check_username = User.objects.get(username=username)
                if check_username:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect(home)
                    else:
                        messages.error(request, 'Oops! Passwords do not match. Please check and try again.')
            
            except ObjectDoesNotExist:
                messages.error(request, 'User not found. Please provide valid credentials for login.')
        return render(request, 'home/user_login.html')
    else:
        return redirect(home)

    
# Register Base Function
def customer_register(request):
    if request.method == 'POST':
        username= request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password'] 
        # chack in password1 or password2 similar 
        if password == con_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Oops! Username is already taken. Please choose another one.')
                return redirect(customer_register)              
            # Field is not Empty
            if username and email and password and con_password:
                user_info=User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
                user_info.save()
                messages.success(request, 'Great job! Your account has been created successfully!')
            else:
                messages.success(request, 'Oops! Please make sure to fill out all the required fields.')                 
        else:
            messages.error(request, 'Oops! Passwords do not match. Please check and try again.')
    return render(request, 'home/customer_register.html')

def seller_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        nid = request.POST['nid']
        password = request.POST['password']
        con_password = request.POST['con_password'] 
        # chack in password1 or password2 similar 
        if password == con_password:
            if User.objects.filter(nid=nid).exists():
                messages.error(request, 'Oops! Username is already taken. Please choose another one.')
                return redirect(customer_register)              
            # Field is not Empty
            if nid and email and password and con_password:
                user_info=User.objects.create_user(username=nid, email=email, first_name=first_name, password=password)
                user_info.save()
                messages.success(request, 'Great job! Your account has been created successfully!')
            else:
                messages.success(request, 'Oops! Please make sure to fill out all the required fields.')                 
        else:
            messages.error(request, 'Oops! Passwords do not match. Please check and try again.')
    return render(request, 'home/seller_register.html')

def user_logout(request):
    logout(request)
    return redirect(home)