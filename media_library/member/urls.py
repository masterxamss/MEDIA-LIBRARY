from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_member_view, name="index"),
    path("books/", views.BooksView.as_view(), name="books"),
    path("cds/", views.CdsView.as_view(), name="cds"),
    path("dvds/", views.DvdsView.as_view(), name="dvds"),
    path("board_games/", views.BoardGamesView.as_view(), name="board_games"),
    path("book/<str:slug>/", views.book_detail, name="book_detail"),
    path("cd/<str:slug>/", views.cd_detail, name="cd_detail"),
    path("dvd/<str:slug>/", views.dvd_detail, name="dvd_detail"),
    path("board_game/<str:slug>/", views.board_game_detail, name="game_detail"),
]