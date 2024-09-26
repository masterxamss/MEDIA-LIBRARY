# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
#from django.utils.text import slugify

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Member
from library.forms import MemberForm


''' CREATE VIEW '''


''' [CBV] - CLASS BASED VIEW '''
class CreateMemberView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'library/members/member_form.html'
    success_url = reverse_lazy('gest-members')


''' [FBV] - FUNCTIONS BASED VIEWS '''
# @login_required
# def CreateBookView(request):
#     """
#     Create a new Book instance.

#     GET:
#     Returns a form to create a new Book instance.

#     POST:
#     Creates a new Book instance with the given data and returns a redirect to
#     the list of books.
#     """
#     form = BookForm()

#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.slug = slugify(book.title)
#             book.save()
#             return redirect('gest-books')

#     context = {
#         'form': form,
#     }
#     return render(request, 'library/books/book_form.html', context)