'''

This view allows you to create a new book in the system.

  *  Ensures that the user is authenticated before allowing book creation.
  *  Uses a form (BookForm) to validate and collect the book's data.
  *  Modifies the book's slug before saving it.
  *  Redirects the user to a success page after the book has been created.

'''

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Book
from library.forms import BookForm


''' CREATE VIEW '''


'''  CLASS BASED VIEW '''
class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books/book_form.html'
    success_url = reverse_lazy('gest-books')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.slug = slugify(book.title)
        book.save()
        return super().form_valid(form)


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