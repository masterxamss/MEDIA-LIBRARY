'''

This view allows you to create a new dv in the system.

  *  Ensures that the user is authenticated before allowing book creation.
  *  Uses a form (DvdForm) to validate and collect the dvd's data.
  *  Modifies the dvd's slug before saving it.
  *  Redirects the user to a success page after the dvd has been created.

'''

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Dvd
from library.forms import DvdForm


''' CREATE VIEW '''


'''  CLASS BASED VIEW '''
class DvdCreateView(LoginRequiredMixin, CreateView):
    model = Dvd
    form_class = DvdForm
    template_name = 'library/dvds/dvd_form.html'
    success_url = reverse_lazy('gest-dvds')

    def form_valid(self, form):
        dvd = form.save(commit=False)
        dvd.slug = slugify(dvd.title)
        dvd.save()
        return super().form_valid(form)


'''  FUNCTIONS BASED VIEWS '''
# @login_required
# def CreateBookView(request):
#     """
#     Create a new Dvd instance.

#     GET:
#     Returns a form to create a new dvd instance.

#     POST:
#     Creates a new Dvd instance with the given data and returns a redirect to
#     the list of dvds.
#     """
#     form = DvdForm()

#     if request.method == 'POST':
#         form = DvdForm(request.POST)
#         if form.is_valid():
#             dvd = form.save(commit=False)
#             dvd.slug = slugify(dvd.title)
#             dvd.save()
#             return redirect('gest-dvds')

#     context = {
#         'form': form,
#     }
#     return render(request, 'library/books/dvd_form.html', context)