from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_library_view, name="home-library"),
]