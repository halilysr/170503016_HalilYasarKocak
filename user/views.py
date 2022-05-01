from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):


    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Successfully registered")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.warning(request, "Wrong user name or password!")
            return render(request, "login.html", context)


        messages.success(request, "Login successful")
        login(request, user)
        return redirect("index") 
    return render(request, "login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("index")
