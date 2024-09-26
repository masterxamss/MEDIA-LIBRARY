from django.urls import path

from library.views import CreateBookView, BooksView, BookDetailView, BookDeleteView, BookUpdateView
from library.views import CreateMemberView, MembersView, MemberDeleteView, MemberUpdateView, MemberDetailView
from library.views import ReservationCreateView, ReservationsView, ReservationDeleteView
from library.views import CdView, CdDetailView, CreateCdView, CdUpdateView, CdDeleteView
from library.views import DvdView, DvdDetailView, DvdCreateView, DvdUpdateView, DvdDeleteView
from library.views import BoardGamesView, BoardGameDetailView, CreateBoardGameView, BoardGameDeleteView, BoardGameUpdateView
from library.views import LoginView, LogoutView
from library.views import HomeView

urlpatterns = [
    # BASE URL
    path("", HomeView, name="home-library"),

    # LOGIN URLS
    path("login/", LoginView, name="login"),
    path("logout/", LogoutView, name="logout"),

    # BOOKS URLS
    path("gest-books/", BooksView.as_view(), name="gest-books"),
    path("create-book/", CreateBookView.as_view(), name="create-book"),
    path("delete-book/<str:slug>/", BookDeleteView.as_view(), name="book-delete"),
    path("update-book/<str:slug>/", BookUpdateView.as_view(), name="book-update"),
    path("detail-book/<str:slug>/",
         BookDetailView.as_view(), name="gest-book-detail"),

    # CDs URLS
    path("gest-cds/", CdView.as_view(), name="gest-cds"),
    path("detail-cd/<str:slug>/", CdDetailView.as_view(), name="gest-cd-detail"),
    path("create-cd/", CreateCdView.as_view(), name="create-cd"),
    path("update-cd/<str:slug>/", CdUpdateView.as_view(), name="update-cd"),
    path("delete-cd/<str:slug>/", CdDeleteView.as_view(), name="delete-cd"),

    # DVDs URLS
    path("gest-dvds/", DvdView.as_view(), name="gest-dvds"),
    path("gest-dvds/<str:slug>/", DvdDetailView.as_view(), name="gest-dvd-detail"),
    path("create-dvd/", DvdCreateView.as_view(), name="create-dvd"),
    path("update-dvd/<str:slug>/", DvdUpdateView.as_view(), name="update-dvd"),
    path("delete-dvd/<str:slug>/", DvdDeleteView.as_view(), name="delete-dvd"),

    # BOARD GAMES URLS
    path("gest-games/", BoardGamesView.as_view(), name="gest-games"),
    path("detail-game/<str:slug>/",
         BoardGameDetailView.as_view(), name="gest-game-detail"),
    path("create-game/", CreateBoardGameView.as_view(), name="create-game"),
    path("update-game/<str:slug>/",
         BoardGameUpdateView.as_view(), name="update-game"),
    path("delete-game/<str:slug>/",
         BoardGameDeleteView.as_view(), name="delete-game"),


    # MEMBERS URLS
    path("gest-members/", MembersView.as_view(), name="gest-members"),
    path("create-member/", CreateMemberView.as_view(), name="create-member"),
    path("delete-member/<int:id>/",
         MemberDeleteView.as_view(), name="delete-member"),
    path("update-member/<int:id>/",
         MemberUpdateView.as_view(), name="update-member"),
    path("detail-members/<int:id>/",
         MemberDetailView.as_view(), name="member-detail"),

    # RESERVATIONS URLS
    path("gest-reservations/", ReservationsView.as_view(),
         name="gest-reservations"),
    path("create-reservation/", ReservationCreateView.as_view(),
         name="create-reservation"),
    path("delete-reservation/<int:id>/",
         ReservationDeleteView.as_view(), name="delete-reservation"),
]
