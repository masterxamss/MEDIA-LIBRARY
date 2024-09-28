# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

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
        try:
            logger.info('Update CD - USER: %s', self.request.user)
            logger.debug(f'CD updated successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception('An error occurred while updating CD: %s', str(e))
            return super().form_invalid(form)


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def CdUpdateView(request, slug):
#     cd = Cd.objects.get(slug=slug)

#     form = CdForm(instance=book)

#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=cd)
#         if form.is_valid():
#             form.save()
#             return redirect('gest-cds') 

#     context = {
#         'form': form
#     }
#     return render(request, 'library/cds/cd_form.html', context)