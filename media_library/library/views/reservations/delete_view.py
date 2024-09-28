from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import MediaReservations
import logging

logger = logging.getLogger('library')

class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = MediaReservations
    template_name = 'library/reservations/reservation_confirm_delete.html'
    success_url = reverse_lazy('gest-reservations')
    pk_url_kwarg = 'id'
    context_object_name = 'reservation'

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to delete a reservation.

        Retrieves the reservation ID from the URL, gets the reservation
        object from the database, and calls its delete method. Logs an info
        message with the user and reservation ID being deleted.

        Args:
            request (HttpRequest): The POST request containing the reservation ID to delete.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the reservation list.

        Logs an info message with the user and reservation ID being deleted.
        Logs an error message with the user and reservation ID if an error occurs.
        """
        self.object = self.get_object()
        try:
            logger.info('User %s is attempting to delete reservation ID: %s', self.request.user, self.object.id)
            logger.debug(f'Details reservation before delete : {self.object}')
            response = self.delete(request, *args, **kwargs)
            logger.info('Reservation deleted successfully')
            return response
        except Exception as e:
            logger.exception('An error occurred while deleting reservation: %s', self.object.id, self.request.user, str(e))
            raise
