from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
import logging

from library.models import MediaReservations
from library.forms import MediaReservationsForm

logger = logging.getLogger('library')

class ReservationCreateView(LoginRequiredMixin, CreateView):

    model = MediaReservations
    form_class = MediaReservationsForm
    template_name = 'library/reservations/reservation_form.html'
    success_url = reverse_lazy('gest-reservations')


    def form_valid(self, form):
        """
        Overrides the form_valid method of CreateView to log the creation of a
        new reservation and the details of the new reservation.

        Args:
            form (MediaReservationsForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and reservation details.
        Logs an error message with the user and reservation ID if an error occurs.
        """
        try:
            logger.info("Create reservation - USER: %s", self.request.user)
            logger.debug(f'Reservation created successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception('Error occurred while creating reservation: %s', str(e))
            return super().form_invalid(form)
