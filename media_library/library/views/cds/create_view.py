# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Cd
from library.forms import CdForm


''' CREATE VIEW '''


'''  CLASS BASED VIEW '''
class CreateCdView(LoginRequiredMixin, CreateView):
    model = Cd
    form_class = CdForm
    template_name = 'library/cds/cd_form.html'
    success_url = reverse_lazy('gest-cds')

    def form_valid(self, form):
        cd = form.save(commit=False)
        cd.slug = slugify(cd.title)
        cd.save()
        return super().form_valid(form)


'''  FUNCTIONS BASED VIEWS '''
# @login_required
# def CreateCdView(request):
#     """
#     Create a new Cd instance.

#     GET:
#     Returns a form to create a new Cd instance.

#     POST:
#     Creates a new Cd instance with the given data and returns a redirect to
#     the list of Cds.
#     """
#     form = CdForm()

#     if request.method == 'POST':
#         form = CdForm(request.POST)
#         if form.is_valid():
#             cd = form.save(commit=False)
#             cd.slug = slugify(book.title)
#             cd.save()
#             return redirect('gest-cds')

#     context = {
#         'form': form,
#     }
#     return render(request, 'library/cds/cd_form.html', context)