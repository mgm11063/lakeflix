from django.urls import path
from movies import views as movie_views

app_name = "core"

# 메인페이지
urlpatterns = [
    path("", movie_views.home_page, name="home"),
]
