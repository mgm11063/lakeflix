from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("test", views.test, name="test"),
    path("<int:pk>", views.movie_detail, name="detail"),
    path("csv_test", views.csv_test, name="csv_test"),
    #path("search/", views.search_view, name="search"),
    path('api/finder/', views.tag_search, name="tag_search"),
]
