from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("test", views.test, name="test"),
    #path("<int:pk>", views.movie_detail, name="detail"),
    #path("search/", views.search_view, name="search"),
]
