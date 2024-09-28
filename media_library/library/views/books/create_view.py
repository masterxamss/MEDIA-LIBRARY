# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Book
from library.forms import BookForm
import logging

logger = logging.getLogger('library')


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books/book_form.html'
    success_url = reverse_lazy('gest-books')

    def form_valid(self, form):
        """
        Overrides the form_valid method of CreateView to log the creation of a
        new Book and the details of the new book.

        Args:
            form (BookForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and book details.
        Logs an error message with the user and book ID if an error occurs.
        """
        try:
            logger.info('Create book - USER: %s', self.request.user)
            book = form.save(commit=False)
            book.slug = slugify(book.title)
            book.save()
            logger.debug(f'Book created: {form.cleaned_data}')
            return super().form_valid(form)
        except Exception as e:
            logger.exception('Error occurred while creating book: %s', str(e))
            return super().form_invalid(form)


'''  FUNCTIONS BASED VIEWS '''
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
