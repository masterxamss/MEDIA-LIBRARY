from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Cd, MediaReservations
from django.contrib import messages

import logging

logger = logging.getLogger('library')


class CdDeleteView(LoginRequiredMixin, DeleteView):
    model = Cd
    template_name = 'library/cds/cd_confirm_delete.html'
    success_url = reverse_lazy('gest-cds')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to delete a cd.

        Retrieves the cd ID from the URL, gets the cd object from the
        database, and calls its delete method. Logs an info message with the
        user and cd ID being deleted.

        Args:
            request (HttpRequest): The POST request containing the cd ID to delete.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the cd list.

        Logs an info message with the user and cd ID being deleted.
        Logs an error message with the user and cd ID if an error occurs.
        """
        self.object = self.get_object()
        try:
            logger.info('User %s is attempting to delete CD ID: %s',
                        self.request.user, self.object.id)
            logger.debug(f'Details cd before delete : {self.object}')

            active_reservations = MediaReservations.objects.filter(cd=self.object, returned=False)

            if active_reservations.exists():
                logger.error('Error deleting CD %s: The CD is present in one or more reservations.',
                            self.object.id)
                messages.error(request, "Ce CD ne peut pas être annulé. Il y a des emprunts qui n'ont pas encore été retournés.")
                return self.render_to_response(self.get_context_data())
            
            response = self.delete(request, *args, **kwargs)
            logger.info('CD deleted successfully')
            return response
        except Exception as e:
            logger.error('Error deleting CD: %s %s', object.id, str(e))
            return redirect('gest-cds')
