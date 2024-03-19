from django.urls import path
from task1 import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
]
