import csv
from operator import mod
from pyexpat import model
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models


def home_page(request):
    all_movies = models.Movies.objects.all()
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/all_movies.html", context={"movies": all_movies})
    else:
        return redirect("/users/login/")


def test(request):
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/subpagetest.html")
    else:
        return redirect("/users/login/")


def movie_detail(request, pk):
    movie = models.Movies.objects.get(pk=pk)
    return render(request, "movies/detail.html", context={"movie": movie})


def csv_test(request):
    CSV_PATH = "/Users/mungyeongmin/lakeflix/JustWatch_dataset_UTF-8.csv"
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            Movies.objects.create(
                title_kor=row['title_kor'],
                year=row['year'],
                genre=row['genre'],
                play_time=row['play_time'],
                director=row['director'],
                justwatch_rating=row['justwatch_rating'],
                imdb_rating=row['imdb_rating'],
                synopsis=row['synopsis'],
                poster=row['poster_src'],
            )

    return HttpResponse("sadfasdfadsffsdaf")
