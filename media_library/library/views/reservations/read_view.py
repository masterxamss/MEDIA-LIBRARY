from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from library.models import MediaReservations
from library.models import Book, Cd, Dvd
import logging

logger = logging.getLogger('library')

class ReservationsView(LoginRequiredMixin,ListView):
    template_name = "library/reservations/gest_reservations.html"
    model = MediaReservations
    ordering = ["-date_requested"]
    context_object_name = "reservations"

    def get_context_data(self, **kwargs):
        """
        Overrides the default ListView get_context_data method to add a list of media items for each reservation.
        
        Args:
            **kwargs: Additional keyword arguments passed to the function.
        
        Returns:
            dict: The context data dictionary with the added media items lists.
        """
        context = super().get_context_data(**kwargs)
        for reservation in context['reservations']:
            reservation.media_items = reservation.get_media_items()
        return context
    

    def post(self, request, *args, **kwargs):     
        """
        Handles a POST request to return a reservation.
        
        Retrieves the reservation ID from the request, gets the reservation
        object from the database, and calls its return_item method. Updates
        the available status of the associated book, DVD or CD.
        
        Args:
            request (HttpRequest): The POST request containing the reservation ID to return.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.
        
        Returns:
            HttpResponse: A redirect response to the reservation list.
        
        Logs an info message with the user and reservation ID being returned.
        Logs an error message with the user and reservation ID if an error occurs.
        """
        try:
            logger.info('User %s is attempting to return reservation ID: %s', self.request.user, request.POST.get('reservation_id'))
            reservation_id = request.POST.get('reservation_id')
            reservation = get_object_or_404(MediaReservations, id=reservation_id)
            reservation.return_item()
            reservation.refresh_from_db()

            if reservation.book:
                Book.update_book_available(reservation.book.id)
            if reservation.dvd:
                Dvd.update_dvd_available(reservation.dvd.id)
            if reservation.cd:
                Cd.update_cd_available(reservation.cd.id)

            logger.debug('Reservation successfully returned by user: %s', self.request.user)
            return redirect(reverse('gest-reservations'))
        except Exception as e:
            logger.error('Error occurred while returning reservation ID %s by user %s: %s', reservation_id, self.request.user, str(e))
            return redirect(reverse('gest-reservations'))
