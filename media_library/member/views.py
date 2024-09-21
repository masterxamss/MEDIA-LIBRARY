from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from library.models import Book, Cd, Dvd, BoardGame

# Create your views here.

def home_member_view(request):
    return render(request, 'member/index.html')



class BooksView(ListView):
    template_name = "member/books.html"
    model = Book
    #ordering = ["-date"]
    context_object_name = "books"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.all()
        return data
    
    
def book_detail(request, slug):
    identified_book = get_object_or_404(Book, slug=slug)
    return render(request, "member/media_detail.html", {
        "book_detail": identified_book,
    })
    

class CdsView(ListView):
    template_name = "member/cds.html"
    model = Cd
    context_object_name = "cds"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.all()
        return data
    
def cd_detail(request, slug):
    identified_cd = get_object_or_404(Cd, slug=slug)
    return render(request, "member/media_detail.html", {
        "cd_detail": identified_cd
    })


class DvdsView(ListView):
    template_name = "member/dvds.html"
    model = Dvd
    context_object_name = "dvds"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.all()
        return data
    

def dvd_detail(request, slug):
    identified_dvd = get_object_or_404(Dvd, slug=slug)
    return render(request, "member/media_detail.html", {
        "dvd_detail": identified_dvd,
    })
    

class BoardGamesView(ListView):
    template_name = "member/board_games.html"
    model = BoardGame
    context_object_name = "board_games"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.all()
        return data
    
def board_game_detail(request, slug):
    identified_game = get_object_or_404(BoardGame, slug=slug)
    return render(request, "member/media_detail.html", {
        "game_detail": identified_game,
    })

