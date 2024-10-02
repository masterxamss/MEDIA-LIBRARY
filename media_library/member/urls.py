from django.urls import path

from library.views import (
    BooksView,
    CdView,
    DvdView,
    BoardGamesView
)

from . import views

urlpatterns = [
    #path("", views.home_member_view, name="index"),
    path("", views.MediaListView.as_view(), name="index"),
    path("books/", BooksView.as_view(), name="books"),
    path("cds/", CdView.as_view(), name="cds"),
    path("dvds/", DvdView.as_view(), name="dvds"),
    path("board_games/", BoardGamesView.as_view(), name="board_games"),
]