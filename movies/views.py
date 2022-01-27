from django.shortcuts import redirect, render


def home_page(request):
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/all_movies.html")
    else:
        return redirect("/users/login/")


def test(request):
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/subpagetest.html")
    else:
        return redirect("/users/login/")
