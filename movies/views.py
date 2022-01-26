from datetime import datetime
from django.shortcuts import render


def all_movies(request):
    now = datetime.now()
    hungry = True
    return render(request, "movies/all_movies.html", context={"haha": now, "hungry": hungry})
