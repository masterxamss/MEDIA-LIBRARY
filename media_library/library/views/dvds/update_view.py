# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import Dvd
from library.forms import DvdForm


''' UPDATE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class DvdUpdateView(LoginRequiredMixin, UpdateView):
    model = Dvd
    form_class = DvdForm
    template_name = 'library/dvds/dvd_form.html'
    slug_field = 'slug'  # Especifica que o lookup será feito pelo campo slug
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-dvds')  # Redireciona após a atualização

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional, se necessário
        return super().form_valid(form)


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