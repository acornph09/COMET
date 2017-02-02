from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from QuiverProject import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user != None:
            if user.is_active:
                login(request, user, backend=None)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "login/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
    return render(request, "login/home.html", {})

def Blog(request):
    return render(request, "login/blog.html", {})

def Register(request):
    next = request.GET.get('next', '/login/')
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'],
                                    email=request.POST['email'],
                                    password=request.POST['password'],
                                    first_name=request.POST['first_name'],
                                    last_name=request.POST['last_name'])
        user.save()
        if user != None:
            return HttpResponseRedirect(next)
        else:
            return render(request, "login/error.html", {})

    return render(request, "login/register.html", {'redirect_to': next})
