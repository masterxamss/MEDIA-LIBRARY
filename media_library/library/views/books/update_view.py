# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import Book
from library.forms import BookForm

import logging

logger = logging.getLogger('library')

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books/book_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-books')

    def form_valid(self, form):
        """
        Overrides the form_valid method of UpdateView to log the update of a
        Book and the details of the updated Book.

        Args:
            form (BookForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and Book details.
        Logs an error message with the user and Book ID if an error occurs.
        """
        try:
            logger.info('Update Book - USER: %s', self.request.user)
            logger.debug(f'Book updated successfully: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception('An error occurred while updating Book: %s', str(e))
            return super().form_invalid(form)


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def BookUpdateView(request, slug):
#     book = Book.objects.get(slug=slug)

#     form = BookForm(instance=book)

#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('gest-books') 

#     context = {
#         'form': form
#     }
#     return render(request, 'library/books/book_form.html', context)