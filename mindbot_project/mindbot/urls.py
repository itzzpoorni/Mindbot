from django.urls import path
from mindbot import views
urlpatterns = [
    path("", views.home, name="home"),
]