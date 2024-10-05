from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Dvd, MediaReservations
from django.contrib import messages

import logging

logger = logging.getLogger('library')


class DvdDeleteView(LoginRequiredMixin, DeleteView):
    model = Dvd
    template_name = 'library/dvds/dvd_confirm_delete.html'
    success_url = reverse_lazy('gest-dvds')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to delete a dvd.

        Retrieves the dvd object from the database, logs an info message with the user and
        dvd ID being deleted, and calls its delete method. Logs an error message with the user
        and dvd ID if an error occurs.

        Checks if the dvd is present in one or more reservations. If it is, logs an error message
        with the user and dvd ID, adds an error message to the request, and renders the form
        again with the error message.

        Args:
            request (HttpRequest): The POST request containing the dvd ID to delete.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the dvd list.

        Logs an info message with the user and dvd ID being deleted.
        Logs an error message with the user and dvd ID if an error occurs.
        """
        self.object = self.get_object()
        try:
            logger.info('User %s is attempting to delete dvd ID: %s',
                        self.request.user, self.object.id)
            logger.debug(f'Details dvd before delete : {self.object}')

            active_reservations = MediaReservations.objects.filter(dvd=self.object, returned=False)

            if active_reservations.exists():
                logger.error('Error deleting DVD %s: The DVD is present in one or more reservations.',
                            self.object.id)
                messages.error(request, "Ce DVD ne peut pas être annulé. Il y a des emprunts qui n'ont pas encore été retournés.")
                return self.render_to_response(self.get_context_data())
            
            response = self.delete(request, *args, **kwargs)
            logger.info('Dvd deleted successfully')
            return response
        except Exception as e:
            logger.error('Error deleting dvd: %s %s', self.object.id, str(e))
            return redirect('gest-dvds')
