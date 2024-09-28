# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import Dvd
from library.forms import DvdForm

import logging


logger = logging.getLogger('library')


class DvdUpdateView(LoginRequiredMixin, UpdateView):
    model = Dvd
    form_class = DvdForm
    template_name = 'library/dvds/dvd_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-dvds')

    def form_valid(self, form):
        """
        Overrides the form_valid method of UpdateView to log the update of a
        Dvd and the details of the updated Dvd.

        Args:
            form (DvdForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and Dvd details.
        Logs an error message with the user and Dvd ID if an error occurs.
        """
        try:
            logger.info('Update dvd - USER: %s', self.request.user)
            logger.debug(f'Dvd updated successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.warning('An error occurred while updating dvd: %s', str(e))
            return super().form_invalid(form)


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def DvdUpdateView(request, slug):
#     dvd = Dvd.objects.get(slug=slug)

#     form = DvdForm(instance=dvd)

#     if request.method == 'POST':
#         form = DvdForm(request.POST, instance=dvd)
#         if form.is_valid():
#             form.save()
#             return redirect('gest-dvds') 

#     context = {
#         'form': form
#     }
#     return render(request, 'library/dvds/dvd_form.html', context)