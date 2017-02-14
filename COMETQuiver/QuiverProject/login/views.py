from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from QuiverProject import settings
from django.contrib.auth.decorators import login_required
from login.models import MyUser
from login.backend import CustomUserAuth
from django.contrib import auth

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = CustomUserAuth.authenticate(username=username, password=password)

        if user != None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect('login/error.html')

    return render(request, "login/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
    return render(request, "login/home.html", {})

def Blog(request):
    return render(request, "login/blog.html", {})

def Success(request):
    return render(request, "login/reg_success.html", {})

def Register(request):
    next = request.GET.get('next', '/reg_success/')
    if request.method == "POST":
        user = MyUser.objects.create_user(
                                    email=request.POST['email'],
                                    password=request.POST['password'],
                                    )
        user.save()
        if user != None:
            return HttpResponseRedirect(next)
        else:
            return render(request, "login/error.html", {})

    return render(request, "login/register.html", {'redirect_to': next})

def LogInError(request):
    return render(request, "login/error.html", {})
