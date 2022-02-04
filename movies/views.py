import csv
import json

from . import models
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login/")
def home_page(request):
    all_movies = models.Movies.objects.all()
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/all_movies.html", context={"movies": all_movies})
    else:
        return redirect(reverse("users:login"))

# @login_required(login_url="/users/login/") =  로그인 안했으면 로그인페이지로 돌리기


@login_required(login_url="/users/login/")
def test(request):
    user = request.user.is_authenticated
    if user:
        return render(request, "movies/subpagetest.html")
    else:
        return redirect(reverse("users:login"))


@login_required(login_url="/users/login/")
def movie_detail(request, pk):
    try:
        movie = models.Movies.objects.get(pk=pk)
        return render(request, "movies/detail.html", context={"movie": movie})

    except models.Movies.DoesNotExist:
        raise Http404()


def tag_search(request):
    all_movies = models.Movies.objects.all()
    all_genres = models.MovieType.objects.all()
    mov_cnt = len(all_movies)
    if request.method == 'GET':
        return render(request, 'movies/tag_search.html', context={'movies': all_movies, "genres": all_genres, "mov_cnt": mov_cnt})
    elif request.method == 'POST':
        checked_movie_type = request.POST.get('movie_type', '') # 체크한 영상의 타입
        filter_attr = request.POST.get('filter_attr', '') # 체크한 영상을 필터링 or 제외할 것인지 값
        print('checked_movie_type =',checked_movie_type, '/ filter_attr =',filter_attr)
        if filter_attr == 'filter':
            # 체크된 태그들만 보여줘. = objects.filter() -> 괄호 안의 값으로 필터링 해 불러옴
            filtered_movies = models.Movies.objects.filter(genre_list__name=checked_movie_type)
        elif filter_attr == 'exclude':
            # 체크된 태그들만 빼고 보여줘 = objects.exclude() 사용 -> 괄호 안의 값을 제외하고 불러옴
            filtered_movies = models.Movies.objects.exclude(genre_list__name=checked_movie_type)
        else: # 해당 태그를 체킹한 카운트가 3이 되는 순간 카운트를 0으로 초기화 시켜줘야 함.
            # 전부 다 보여줘 = all_movies
            filtered_movies = all_movies

        # QuerySet 타입을 json으로 넘길 수 있도록 안의 값을 빼서 리스트화.
        context = {'movies': list(filtered_movies.values())}
        print(type(context), context)

        return HttpResponse(json.dumps(context), content_type='application/json')
        # return render(request, 'movies/tag_search.html', context={'movies': filtered_movies, "genres": all_genres})


def csv_test(request):
    CSV_PATH = "/JustWatch_dataset.csv"
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:

            genre_data = row['genre_list']
            # genre_data_list 수정 필요 너무 replace 불필요하게 많이 사용함
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
