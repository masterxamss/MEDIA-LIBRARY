from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from library.models import MediaReservations
from library.forms import MediaReservationsForm

class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = MediaReservations
    form_class = MediaReservationsForm
    template_name = 'library/reservations/reservation_form.html'
    success_url = reverse_lazy('gest-reservations')

    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.save()
        return super().form_valid(form)