from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from library.models import Book, Cd, Dvd, BoardGame



def home_member_view(request):
    return render(request, 'member/index.html')


# -----------------------------------------------------------
# BOOKS VIEWS
# -----------------------------------------------------------
class MemberBooksView(ListView):
    template_name = "member/books.html"
    model = Book
    ordering = ["title"]
    context_object_name = "books"
    paginate_by = 10


def MemberBookDetail(request, slug):
    identified_media = get_object_or_404(Book, slug=slug)
    return render(request, "member/media_detail.html", {
        "book_detail": identified_media
    })


# -----------------------------------------------------------
# CDS VIEWS
# -----------------------------------------------------------
class CdsView(ListView):
    template_name = "member/cds.html"
    model = Cd
    ordering = ["title"]
    context_object_name = "cds"
    paginate_by = 10


def cd_detail(request, slug):
    identified_media = get_object_or_404(Cd, slug=slug)
    return render(request, "member/media_detail.html", {
        "cd_detail": identified_media
    })


# -----------------------------------------------------------
# DVDS VIEWS
# -----------------------------------------------------------
class DvdsView(ListView):
    template_name = "member/dvds.html"
    model = Dvd
    ordering = ["title"]
    context_object_name = "dvds"
    paginate_by = 10


def dvd_detail(request, slug):
    identified_media = get_object_or_404(Dvd, slug=slug)
    return render(request, "member/media_detail.html", {
        "dvd_detail": identified_media,
    })


# -----------------------------------------------------------
# BOARD GAMES VIEWS
# -----------------------------------------------------------
class BoardGamesView(ListView):
    template_name = "member/board_games.html"
    model = BoardGame
    ordering = ["name"]
    context_object_name = "board_games"
    paginate_by = 10


def board_game_detail(request, slug):
    identified_media = get_object_or_404(BoardGame, slug=slug)
    return render(request, "member/media_detail.html", {
        "game_detail": identified_media,
    })
