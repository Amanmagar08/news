from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
path("", views.home, name="home"),
path("about", views.about, name = "about"),
path('newsDetails/<int:id>', views.newsDetails, name = "newsDetails"),
path("login", views.loginPage, name="")
]