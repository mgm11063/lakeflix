from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("test", views.test, name="test"),
    path("<int:pk>", views.movie_detail, name="detail"),
    # csv파일 DB테이블 만들때 사용하는것 ! 주의해서 사용 path("csv_test", views.csv_test, name="csv_test"),
    #path("search/", views.search_view, name="search"),
]
