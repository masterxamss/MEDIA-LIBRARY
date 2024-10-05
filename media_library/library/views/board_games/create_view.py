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
        """
        Overrides the form_valid method of CreateView to log the creation of a
        new board game and the details of the new board game.

        Args:
            form (BoardGameForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and board game details.
        Logs an error message with the user and board game ID if an error occurs.
        """
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
