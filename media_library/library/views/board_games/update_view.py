from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import BoardGame
from library.forms import BoardGameForm

import logging

logger = logging.getLogger('library')


class BoardGameUpdateView(LoginRequiredMixin, UpdateView):
    model = BoardGame
    form_class = BoardGameForm
    template_name = 'library/board_games/board_game_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-games')

    def form_valid(self, form):
        """
        Overrides the form_valid method of UpdateView to log the update of a
        Board Game and the details of the updated Board Game.

        Args:
            form (BoardGameForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and Board Game details.
        Logs an error message with the user and Board Game ID if an error occurs.
        """
        try:
            logger.info('Update board game - USER: %s', self.request.user)
            logger.debug(
                f'Board game updated successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception(
                'An error occurred while updating board game: %s', str(e))
            return super().form_invalid(form)
