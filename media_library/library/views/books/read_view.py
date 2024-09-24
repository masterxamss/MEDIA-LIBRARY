#from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import Book


''' READ VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class BooksView(LoginRequiredMixin,ListView):
    template_name = "library/books/gest_books.html"
    model = Book
    ordering = ["title"]
    context_object_name = "books"
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "library/gest_media.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'book_detail'


''' [FBV] - FUNCTIONS BASED VIEWs '''
# @login_required
# def LibraryBooksView(request):
#     books = Book.objects.all()
#     context = {
#         'books': books
#     }
#     return render(request, 'library/books/gest_books.html', context)

# @login_required
# def LibraryBookDetailView(request, slug):
#     identified_media = get_object_or_404(Book, slug=slug)
#     return render(request, "library/gest_media.html", {
#         "book_detail": identified_media
#     })