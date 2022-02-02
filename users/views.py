from . models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout


def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html')
    elif request.method == 'POST':
        avatar = request.POST.get("avatar", None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        password2 = request.POST.get("password2", None)
        firstname = request.POST.get("firstname", None)
        lastname = request.POST.get("lastname", None)
        email = request.POST.get("email", None)
        gender = request.POST.get("gender", None)
        bio = request.POST.get("bio", None)

        if password != password2:
            return redirect(reverse("users:signup"))

        else:
            exist_user = User.objects.filter(username=username)
            if exist_user:
                return redirect(reverse("users:signup"))

            else:
                User.objects.create_user(
                    avatar=avatar,
                    username=username,
                    password=password,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    bio=bio,
                    gender=gender,
                )
            return redirect(reverse("users:login"))


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        get_user = auth.authenticate(
            request, username=username, password=password)
        if get_user is not None:
            auth.login(request, get_user)
            return redirect("/")
        else:
            return redirect(reverse("users:login"))
    elif request.method == 'GET':
        return render(request, 'users/login.html')


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
