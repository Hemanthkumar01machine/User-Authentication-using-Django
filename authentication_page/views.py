from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

def home(request):
    return render(request,"base.html")

def login(request):
    if request.method=="POST":
        name=request.POST["name"]
        p=request.POST["password"]

        user=auth.authenticate(username=name,password=p)

        if user is not None:
            return render(request,"authentication_true.html",{"user":user})
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/")
    else:
        return render(request,"login.html")


def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]

        if password==confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect(register)
            else:
                user=User.objects.create_user(username=name, email=email, password=password)
                user.save()
        else:
            messages.info(request,"Password dosen't Match")
            return redirect(register)

        messages.info(request,"Account Created Successfully")
        return redirect("/")

    else:
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")



