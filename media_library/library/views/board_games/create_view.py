# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import BoardGame
from library.forms import BoardGameForm

import logging

logger = logging.getLogger('library')


class CreateBoardGameView(LoginRequiredMixin, CreateView):
    model = BoardGame
    form_class = BoardGameForm
    template_name = 'library/board_games/board_game_form.html'
    success_url = reverse_lazy('gest-games')

    def form_valid(self, form):
        try:
            logger.info('Create board game - USER: %s', self.request.user)
            board_game = form.save(commit=False)
            board_game.slug = slugify(board_game.name)
            board_game.save()
            logger.debug(
                f'Board game created successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception(
				'An error occurred while creating board game: %s', str(e))
            return super().form_invalid(form)


'''  FUNCTIONS BASED VIEWS '''
# @login_required
# def CreateBoardGameView(request):
#     """
#     Create a new BoardGame instance.

#     GET:
#     Returns a form to create a new BoardGame instance.

#     POST:
#     Creates a new BoardGame instance with the given data and returns a redirect to
#     the list of board_games.
#     """
#     form = BoardGameForm()

#     if request.method == 'POST':
#         form = BoardGameForm(request.POST)
#         if form.is_valid():
#             board_game = form.save(commit=False)
#             board_game.slug = slugify(board_game.name)
#             board_game.save()
#             return redirect('gest-games')

#     context = {
#         'form': form,
#     }
#     return render(request, 'library/board_games/board_game_form.html', context)
