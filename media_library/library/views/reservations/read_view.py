from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from library.models import MediaReservations
from library.models import Book, Cd, Dvd

class ReservationsView(LoginRequiredMixin,ListView):
    template_name = "library/reservations/gest_reservations.html"
    model = MediaReservations
    ordering = ["-date_requested"]
    context_object_name = "reservations"
    paginate_by = 10

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
        Marks a reservation as returned and updates the availability of the associated media item.

        Args:
            request (HttpRequest): The request that triggered this function.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect to the list of reservations.
        """
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
        
        return redirect(reverse('gest-reservations'))
