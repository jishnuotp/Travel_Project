from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credentials is invalid')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['Username']
        first_name=request.POST['First_name']
        last_name=request.POST['Last_name']
        email = request.POST['Email']
        password = request.POST['Password']
        cpassword = request.POST['Cpassword']

        if password == cpassword :
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username is already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email already used")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matched")
            return redirect('register')

    return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
