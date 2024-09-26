# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Dvd


''' DELETE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class DvdDeleteView(LoginRequiredMixin, DeleteView):
    model = Dvd
    template_name = 'library/dvds/dvd_confirm_delete.html'
    success_url = reverse_lazy('gest-dvds')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


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