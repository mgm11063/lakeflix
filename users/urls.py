from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.sign_up_view, name="signup"),
]
