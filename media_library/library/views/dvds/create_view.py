from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Dvd
from library.forms import DvdForm

import logging

logger = logging.getLogger('library')


class DvdCreateView(LoginRequiredMixin, CreateView):
    model = Dvd
    form_class = DvdForm
    template_name = 'library/dvds/dvd_form.html'
    success_url = reverse_lazy('gest-dvds')

    def form_valid(self, form):
        """
        Overrides the form_valid method of CreateView to log the creation of a
        new Dvd and the details of the new Dvd.

        Args:
            form (DvdForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and Dvd details.
        Logs an error message with the user and Dvd ID if an error occurs.
        """
        try:
            logger.info('Create dvd - USER: %s', self.request.user)
            dvd = form.save(commit=False)
            dvd.slug = slugify(dvd.title)
            dvd.save()
            logger.debug(f'Dvd created successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception(
                'An error occurred while creating dvd: %s', str(e))
            return super().form_invalid(form)
