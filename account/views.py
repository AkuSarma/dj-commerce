from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if  request.method == "POST":
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect('register')
        
        get_all_users_by_username  = User.objects.filter(username=userName).exists()
        if get_all_users_by_username:
            messages.error(request, "Username already exists")
            return redirect('register')

        newUser = User.objects.create_user(username=userName, email=email, password=password)
        newUser.save()

        messages.success(request, "User successfully created, Login now")
        redirect('login')

    return render(request,'account/register.html', {})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get( 'username' )
        password = request.POST.get( 'password' )
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            messages.info(request,"You are  now logged in.")
            return redirect("home-page")
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'account/login.html', {})

def logout_page(request):
    logout(request)
    return redirect('login')