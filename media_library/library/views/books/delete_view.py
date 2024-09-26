# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Book


''' DELETE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/books/book_confirm_delete.html'
    success_url = reverse_lazy('gest-books')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def BookDeleteView(request, slug):
#     book = Book.objects.get(slug=slug)

#     if book.method == 'POST':
#         book.delete()
#         return redirect('gest-books')

#     context = {
#         'book': book
#     }
#     return render(request, 'library/books/book_confirm_delete.html', context)