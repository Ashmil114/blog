from django.urls import path
from .views import login_view, registration, logout_view

urlpatterns = [
    path("login", login_view, name="login"),
    path("register", registration, name="register"),
    path("logout/", logout_view, name="logout"),
]
