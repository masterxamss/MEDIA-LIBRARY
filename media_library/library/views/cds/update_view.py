# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import Cd
from library.forms import CdForm


''' UPDATE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class CdUpdateView(LoginRequiredMixin, UpdateView):
    model = Cd
    form_class = CdForm
    template_name = 'library/cds/cd_form.html'
    slug_field = 'slug'  # Especifica que o lookup será feito pelo campo slug
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-cds')  # Redireciona após a atualização

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional, se necessário
        return super().form_valid(form)


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