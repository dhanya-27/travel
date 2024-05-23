from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        Username=request.POST['username']
        Password=request.POST['password']
        user=auth.authenticate(username=Username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Firstname = request.POST['first_name']
        Lastname = request.POST['last_name']
        Email = request.POST['email']
        Password = request.POST['password']
        Conpassword = request.POST['password1']
        if Password == Conpassword:
            if User.objects.filter(username=Username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=Username, first_name=Firstname, last_name=Lastname,
                                                email=Email,
                                                password=Password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request, user=None):
    auth.login(request,user)
    return render(request,"login.html")