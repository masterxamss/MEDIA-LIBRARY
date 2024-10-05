from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Cd
from library.forms import CdForm

import logging


logger = logging.getLogger('library')


class CreateCdView(LoginRequiredMixin, CreateView):
    model = Cd
    form_class = CdForm
    template_name = 'library/cds/cd_form.html'
    success_url = reverse_lazy('gest-cds')

    def form_valid(self, form):
        """
        Overrides the form_valid method of CreateView to log the creation of a
        new CD and the details of the new CD.

        Args:
            form (CdForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and CD details.
        Logs an error message with the user and CD ID if an error occurs.
        """
        try:
            logger.info('Create CD - USER: %s', self.request.user)
            cd = form.save(commit=False)
            cd.slug = slugify(cd.title)
            cd.save()
            logger.debug(f'CD created successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception('An error occurred while creating CD: %s', str(e))
            return super().form_invalid(form)
