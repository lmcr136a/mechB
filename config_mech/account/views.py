from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.


def home_view(request):
    return render(request, 'html/Home.html',{})


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            auth.login(request, user)
            return redirect('account:home_view')
        return render(request, 'html/signup.html', {'error': 'Incorrect password'})
    return render(request, 'html/signup.html', {'error': 'Something goes wrong!'})


def login(request):
    if request.method == "POST":
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('account:home_view')
        else:
            return render(request, 'html/re_login.html', {'error': 'username of password is incorrect!!!'})
    else:
        return render(request, 'html/re_login.html', {})


def login_pg(request):
    return render(request, 'html/login.html', {})


def signup_pg(request):
    return render(request, 'html/signup.html', {})


def logout(request):
    auth.logout(request)
    return redirect('account:login_pg')