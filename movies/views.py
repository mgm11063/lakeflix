from datetime import datetime
from django.shortcuts import render


def all_movies(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_movies.html", context={"now": now, "hungry": hungry})
