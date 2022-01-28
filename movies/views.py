from django.shortcuts import redirect, render
from django.http import HttpResponse

import csv

from movies.models import Movies


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


def csv_test(request):
    CSV_PATH = "/Users/mungyeongmin/lakeflix/JustWatch_dataset_UTF-8.csv"
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            print(row)
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
