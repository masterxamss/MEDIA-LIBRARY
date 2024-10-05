from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import Cd
from library.forms import CdForm

import logging

logger = logging.getLogger('library')


class CdUpdateView(LoginRequiredMixin, UpdateView):
    model = Cd
    form_class = CdForm
    template_name = 'library/cds/cd_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-cds')

    def form_valid(self, form):
        """
        Overrides the form_valid method of UpdateView to log the update of a
        CD and the details of the updated CD.

        Args:
            form (CdForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and CD details.
        Logs an error message with the user and CD ID if an error occurs.
        """
        try:
            logger.info('Update CD - USER: %s', self.request.user)
            logger.debug(f'CD updated successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception('An error occurred while updating CD: %s', str(e))
            return super().form_invalid(form)
