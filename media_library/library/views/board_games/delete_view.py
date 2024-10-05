from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import BoardGame
from django.shortcuts import redirect


import logging

logger = logging.getLogger('library')


class BoardGameDeleteView(LoginRequiredMixin, DeleteView):
    model = BoardGame
    template_name = 'library/board_games/board_game_confirm_delete.html'
    success_url = reverse_lazy('gest-games')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'board_game'

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to delete a BoardGame.

        Retrieves the BoardGame ID from the URL, gets the BoardGame object from the
        database, and calls its delete method. Logs an info message with the
        user and BoardGame ID being deleted.

        Args:
            request (HttpRequest): The POST request containing the BoardGame ID to delete.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the BoardGame list.

        Logs an info message with the user and BoardGame ID being deleted.
        Logs an error message with the user and BoardGame ID if an error occurs.
        """
        self.object = self.get_object()
        try:
            logger.info('User %s is attempting to delete BoardGame ID: %s',
                        self.request.user, self.object.id)
            logger.debug(f'Details board_game before delete : {self.object}')
            response = self.delete(request, *args, **kwargs)
            logger.info('BoardGame deleted successfully')
            return response
        except Exception as e:
            logger.error('Error deleting BoardGame: %s %s', object.id, str(e))
            return redirect('gest-games')
