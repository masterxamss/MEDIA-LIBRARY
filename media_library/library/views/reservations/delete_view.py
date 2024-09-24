from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import MediaReservations

class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = MediaReservations
    template_name = 'library/reservations/reservation_confirm_delete.html'
    success_url = reverse_lazy('gest-reservations')
    pk_url_kwarg = 'id'
    context_object_name = 'reservation'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)