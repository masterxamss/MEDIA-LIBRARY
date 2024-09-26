# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import BoardGame


class BoardGamesView(LoginRequiredMixin,ListView):
    template_name = "library/board_games/gest_board_games.html"
    model = BoardGame
    ordering = ["name"]
    context_object_name = "board_games"
    paginate_by = 10

class BoardGameDetailView(LoginRequiredMixin, DetailView):
    model = BoardGame
    template_name = "library/gest_media.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'game_detail'

# @login_required
# def LibraryBoardGamesDetailView(request, slug):
#     identified_media = get_object_or_404(BoardGame, slug=slug)
#     return render(request, "library/gest_media.html", {
#         "game_detail": identified_media
#     })
