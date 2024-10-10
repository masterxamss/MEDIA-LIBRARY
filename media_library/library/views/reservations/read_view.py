from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from library.models import MediaReservations
from library.models import Book, Cd, Dvd
from django.db.models import Q
import logging

logger = logging.getLogger('library')


class ReservationsView(LoginRequiredMixin, ListView):
    template_name = "library/reservations/gest_reservations.html"
    model = MediaReservations
    ordering = ["id"]
    paginate_by = 10
    context_object_name = "reservations"

    error = None

    def get_queryset(self):
        """
        Override the default queryset to apply filtering based on the POST request.

        Retrieves the reservations from the database and applies the filters based on
        the POST request. If the search_member field is not empty, filters the
        reservations by the search_member field. If the return_all field is checked,
        does not apply any additional filtering. If the return_active field is
        checked, filters the reservations by those that are not returned. If the
        return_completed field is checked, filters the reservations by those that are
        returned. If the asc_date field is checked, orders the reservations by the
        date_requested field in ascending order. If the desc_date field is checked,
        orders the reservations by the date_requested field in descending order.
        """
        queryset = super().get_queryset()

        # Get POST parameters if any
        search_member = self.request.POST.get('search_member', '').strip()
        returm_all = self.request.POST.get('return_all')
        return_active = self.request.POST.get('return_active')
        return_completed = self.request.POST.get('return_completed')
        asc_date = self.request.POST.get('asc_date')
        desc_date = self.request.POST.get('desc_date')

        # Apply filters based on POST data
        if search_member:
            queryset = queryset.filter(
                Q(member__first_name__icontains=search_member) | Q(
                    member__last_name__icontains=search_member)
            )
            if queryset.count() == 0:
                self.error = "Aucun emprunt trouvé."

        if returm_all:
            pass

        if return_active:
            queryset = queryset.filter(returned=False)
            if queryset.count() == 0:
                self.error = "Pas d'emprunt actif trouvé."

        if return_completed:
            queryset = queryset.filter(returned=True)
            if queryset.count() == 0:
                self.error = "Aucun emprunt complété n'a été trouvé."

        if asc_date:
            queryset = queryset.order_by('date_requested')

        if desc_date:
            queryset = queryset.order_by('-date_requested')

        return queryset
    

    def get(self, request, *args, **kwargs):
        """
        Handles a GET request to display the list of reservations.

        Retrieves all the reservations that are not returned from the database.
        For each reservation, checks if it is late and if so, sets the error
        message of the view.
        """
        reservations = MediaReservations.objects.filter(returned=False)

        for reservation in reservations:
            reservation.is_late()

        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to return a reservation.

        Retrieves the reservation ID from the request, gets the reservation
        object from the database, and calls its return_item method. If the
        reservation was for a book, calls the update_book_available method
        of the Book model. If the reservation was for a DVD, calls the
        update_dvd_available method of the Dvd model. If the reservation was
        for a CD, calls the update_cd_available method of the Cd model.
        Logs an info message with the user and reservation ID being returned.
        Logs an error message with the user and reservation ID if an error
        occurs.

        Args:
            request (HttpRequest): The POST request containing the reservation ID to return.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the reservation list.

        Logs an info message with the user and reservation ID being returned.
        Logs an error message with the user and reservation ID if an error occurs.
        """
        if request.POST.get('reservation_id'):
            try:
                logger.info('User %s is attempting to return reservation ID: %s',
                            self.request.user, request.POST.get('reservation_id'))
                reservation_id = request.POST.get('reservation_id')
                reservation = get_object_or_404(
                    MediaReservations, id=reservation_id)
                reservation.return_item()
                reservation.refresh_from_db()

                if reservation.book:
                    Book.update_book_available(reservation.book.id)
                if reservation.dvd:
                    Dvd.update_dvd_available(reservation.dvd.id)
                if reservation.cd:
                    Cd.update_cd_available(reservation.cd.id)

                logger.debug(
                    'Reservation successfully returned by user: %s', self.request.user)
                return redirect(reverse('gest-reservations'))
            except Exception as e:
                logger.error('Error occurred while returning reservation ID %s by user %s: %s',
                             reservation_id, self.request.user, str(e))
                return redirect(reverse('gest-reservations'))

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the response.

        Adds the error message if any, total reservations, total active reservations,
        total completed reservations, and the status of the filters and sorting options.

        Returns:
            dict: The context as a dictionary.
        """
        context = super().get_context_data(**kwargs)

        reservations = MediaReservations.objects.all()
        for reservation in context['reservations']:
            reservation.media_items = reservation.get_media_items()

        context['error'] = self.error
        context['total_reservations'] = reservations.count()
        context['total_reservations_active'] = reservations.filter(
            returned=False).count()
        context['total_reservations_completed'] = reservations.filter(
            returned=True).count()
        context['return_all'] = 'checked' if self.request.POST.get(
            'return_all') else ''
        context['return_active'] = 'checked' if self.request.POST.get(
            'return_active') else ''
        context['return_completed'] = 'checked' if self.request.POST.get(
            'return_completed') else ''
        context['asc_date'] = 'checked' if self.request.POST.get(
            'asc_date') else ''
        context['desc_date'] = 'checked' if self.request.POST.get(
            'desc_date') else ''

        return context
