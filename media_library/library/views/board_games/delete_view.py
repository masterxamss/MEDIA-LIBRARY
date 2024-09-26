# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import BoardGame


''' DELETE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class BoardGameDeleteView(LoginRequiredMixin, DeleteView):
    model = BoardGame
    template_name = 'library/board_games/board_game_confirm_delete.html'
    success_url = reverse_lazy('gest-games')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'board_game'


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def BoardGameDeleteView(request, slug):
#     board_game = BoardGame.objects.get(slug=slug)

#     if board_game.method == 'POST':
#         board_game.delete()
#         return redirect('gest-games')

#     context = {
#         'board_game': board_game
#     }
#     return render(request, 'library/board_games/board_game_confirm_delete.html', context)