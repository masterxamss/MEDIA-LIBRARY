from django.urls import path

from . import views

urlpatterns = [
    # BASE URL
    path("", views.HomeLibraryView, name="home-library"),

    # LOGIN URLS
    path("login/", views.LoginView, name="login"),
    path("logout/", views.LogoutView, name="logout"),

    # BOOKS URLS
    path("create-book/", views.CreateBookView.as_view(), name="create-book"),
    path("gest-books/", views.LibraryBooksView.as_view(), name="gest-books"),
    path("book-delete/<str:slug>/", views.BookDeleteView.as_view(), name="book-delete"),
    path("book-update/<str:slug>/", views.BookUpdateView.as_view(), name="book-update"),
    path("gest-books/<str:slug>/", views.LibraryBookDetailView.as_view(), name="gest-book-detail"),

    # CDs URLS
    path("gest-cds/", views.LibraryCdView.as_view(), name="gest-cds"),
    path("gest-cds/<str:slug>/", views.LibraryCdDetailView, name="gest-cd-detail"),

    # DVDs URLS
    path("gest-dvds/", views.LibraryDvdView.as_view(), name="gest-dvds"),
    path("gest-dvds/<str:slug>/", views.LibraryDvdDetailView, name="gest-dvd-detail"),

    # BOARD GAMES URLS
    path("gest-games/", views.LibraryBoardGamesView.as_view(), name="gest-games"),
    path("gest-games/<str:slug>/", views.LibraryBoardGamesDetailView, name="gest-game-detail"),
]