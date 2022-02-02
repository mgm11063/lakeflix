import csv
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import models


@login_required(login_url="/users/login/")
def home_page(request):
    all_movies = models.Movies.objects.all()
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/all_movies.html", context={"movies": all_movies})
    else:
        return redirect("/users/login/")

# @login_required(login_url="/users/login/") =  로그인 안했으면 로그인페이지로 돌리기


@login_required(login_url="/users/login/")
def test(request):
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/subpagetest.html")
    else:
        return redirect("/users/login/")


@login_required(login_url="/users/login/")
def movie_detail(request, pk):
    movie = models.Movies.objects.get(pk=pk)
    return render(request, "movies/detail.html", context={"movie": movie})


def csv_test(request):
    CSV_PATH = "/Users/mungyeongmin/lakeflix/JustWatch_dataset.csv"
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:

            genre_data = row['genre_list']
            genre_data_list = genre_data.replace("[", "").replace(
                "]", "").replace(" ", "").replace("'", "").split(",")

            movies, _ = models.Movies.objects.get_or_create(
                title_kor=row['title_kor'],
                year=row['year'],
                play_time=row['play_time'],
                director=row['director'],
                justwatch_rating=row['justwatch_rating'],
                imdb_rating=row['imdb_rating'],
                synopsis=row['synopsis'],
                poster=row['poster_src'],
            )

            # 데이터 셋에 장르를 걸러서 장르 타입에 올린다
            for genre in genre_data_list:
                MovieGenre, _ = models.MovieType.objects.get_or_create(
                    name=genre
                )
                movies.genre_list.add(MovieGenre)

    return HttpResponse("여기는 데이터 셋을 DB에 업로드 하는 곳입니다! 업로드 할때를 제외하고는 와서는 안되는 페이지 입니다!! 여기로 올시 경민님께 말씀해주세요!")
