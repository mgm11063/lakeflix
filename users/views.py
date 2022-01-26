# user/views.py
from django.shortcuts import render, redirect
from . models import User
from django.http import HttpResponse


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
            return render(request, 'users/signup.html')
        else:
            user = User()
            user.avatar = avatar
            user.username = username
            user.password = password
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.bio = bio
            user.gender = gender
            user.save()
        return redirect("/users/login/")


def login_view(request):
    if request.method == 'POST':
        return HttpResponse("로그인 성공 ")
    elif request.method == 'GET':
        return render(request, 'users/login.html')
