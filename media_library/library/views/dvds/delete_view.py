# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Dvd

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
        Handles a POST request to delete a Dvd.

        Retrieves the Dvd ID from the URL, gets the Dvd object from the
        database, and calls its delete method. Logs an info message with the
        user and Dvd ID being deleted.

        Args:
            request (HttpRequest): The POST request containing the Dvd ID to delete.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the Dvd list.

        Logs an info message with the user and Dvd ID being deleted.
        Logs an error message with the user and Dvd ID if an error occurs.
        """
        self.object = self.get_object()
        try:
            logger.info('User %s is attempting to delete dvd ID: %s', self.request.user, self.object.id)
            logger.debug(f'Details dvd before delete : {self.object}')
            response = self.delete(request, *args, **kwargs)
            logger.info('Dvd deleted successfully')
            return response
        except Exception as e:
            logger.error('Error deleting dvd: %s %s', self.object.id, str(e))
            return redirect('gest-dvds')


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def DvdDeleteView(request, slug):
#     dvd = Dvd.objects.get(slug=slug)

#     if dvd.method == 'POST':
#         dvd.delete()
#         return redirect('gest-dvds')

#     context = {
#         'dvd': dvd
#     }
#     return render(request, 'library/dvds/dvd_confirm_delete.html', context)