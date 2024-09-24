from django.urls import path

from library.views.books import CreateBookView, BooksView, BookDetailView, BookDeleteView, BookUpdateView
from library.views.members import CreateMemberView, MembersView, MemberDeleteView, MemberUpdateView, MemberDetailView
from library.views.reservations import ReservationCreateView, ReservationsView, ReservationDeleteView
from library.views.cds import CdView, CdDetailView
from library.views.dvds import DvdView, DvdDetailView
from library.views.board_games import BoardGamesView, BoardGameDetailView
from library.views.login import LoginView, LogoutView
from library.views.home import HomeView

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

    # DVDs URLS
    path("gest-dvds/", DvdView.as_view(), name="gest-dvds"),
    path("gest-dvds/<str:slug>/", DvdDetailView.as_view(), name="gest-dvd-detail"),

    # BOARD GAMES URLS
    path("gest-games/", BoardGamesView.as_view(), name="gest-games"),
    path("detail-game/<str:slug>/",
         BoardGameDetailView.as_view(), name="gest-game-detail"),

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
