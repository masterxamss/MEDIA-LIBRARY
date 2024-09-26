# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Cd


''' DELETE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class CdDeleteView(LoginRequiredMixin, DeleteView):
    model = Cd
    template_name = 'library/cds/cd_confirm_delete.html'
    success_url = reverse_lazy('gest-cds')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def CdDeleteView(request, slug):
#     cd = Cd.objects.get(slug=slug)

#     if cd.method == 'POST':
#         cd.delete()
#         return redirect('gest-cds')

#     context = {
#         'cd': cd
#     }
#     return render(request, 'library/cds/cd_confirm_delete.html', context)