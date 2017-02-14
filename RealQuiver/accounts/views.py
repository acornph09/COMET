from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from RealQuiver import settings
from django.contrib.auth.decorators import login_required
from accounts.admin import UserCreationForm
from accounts.forms import LoginForm
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)
from django.contrib import auth

def Register(request):
    reg_form = UserCreationForm(request.POST or None)
    context = {
        "title": "Quiver Sign-Up",
        "form": reg_form,
    }
    print(reg_form.is_valid())
    if reg_form.is_valid():
        email = reg_form.cleaned_data.get("email")
        first_name = reg_form.cleaned_data.get("first_name")
        middle_name = reg_form.cleaned_data.get("middle_name")
        last_name = reg_form.cleaned_data.get("last_name")
        password1 = reg_form.cleaned_data.get("password1")
        password2 = reg_form.cleaned_data.get("password2")
        user=reg_form.save()
        return render(request, 'accounts/login.html', {})
    return render(request, 'accounts/register.html', context)



def login_view(request):
    form = LoginForm(data=request.POST)
    if request.method == 'POST':

        context = {
            "title": "Quiver Sign-Up",
            "form": form
        }
        print(form.is_valid())
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return render(request, 'accounts/homescreen.html')
            else:
                return render(request, 'accounts/error.html')
        else:
            render(request, 'accounts/error.html', context)

    return render(request, 'accounts/login.html', {
            "title": "Quiver Sign-Up",
            "form": form,
            "next": next,
        })

'''
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user != None:
            if user.is_active:
                accounts(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect('accounts/error.html')

    return render(request, "accounts/accounts.html", {'redirect_to': next})
'''
def logout_view(request):
    logout(request)
    form = LoginForm(data=request.POST)
    if request.method == 'POST':

        context = {
            "title": "Quiver Sign-Up",
            "form": form
        }
        print(form.is_valid())
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return render(request, 'accounts/homescreen.html')
            else:
                return render(request, 'accounts/error.html')
        else:
            render(request, 'accounts/error.html', context)

    return render(request, 'accounts/login.html', {
        "title": "Quiver Sign-Up",
        "form": form,
        "next": next,
    })
    return render(request, "accounts/login.html", {})

def login_error(request):
    return render(request, "accounts/error.html", {'user':request.user})


@login_required
def homescreen(request):
    return render(request, "accounts/homescreen.html", {'user':request.user})



def Blog(request):
    return render(request, "accounts/blog.html", {})



def Success(request):
    return render(request, "accounts/reg_success.html", {})


'''
def Register(request):
   next = request.GET.get('next', '/reg_success/')
    if request.method == "POST":
        reg_form = UserCreationForm()
        context = {
            "title": "Quiver Registration",
            "form": reg_form
        }


        user = CustomUser.objects.create_user(
                                    email=request.POST['email'],
                                    password=request.POST['password'],
                                    )
        user.save()
        if user != None:
            return HttpResponseRedirect(next)
        else:
            return render(request, "accounts/error.html", {})

    return render(request, "accounts/register.html", {'redirect_to': next})
'''

