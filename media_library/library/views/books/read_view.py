from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import Book


class BooksView(LoginRequiredMixin, ListView):
    template_name = "library/books/gest_books.html"
    model = Book
    ordering = ["title"]
    paginate_by = 10
    context_object_name = "books"

    error = None

    def get_queryset(self):
        """
        Override the default queryset to apply filtering based on the POST request.
        """
        queryset = super().get_queryset()
        
        # Get POST parameters if any
        search_title = self.request.POST.get('search_title', '').strip()
        return_availables = self.request.POST.get('return_availables')
        return_unavailables = self.request.POST.get('return_unavailables')

        # Apply filters based on POST data
        if search_title:
            queryset = queryset.filter(title__icontains=search_title)
            if queryset.count() == 0:
                self.error = "Aucun livre ne correspond à votre recherche."
        elif return_availables:
            queryset = queryset.filter(available=True)
            if queryset.count() == 0:
                self.error = "Aucun livre n'est disponible."
        elif return_unavailables:
            queryset = queryset.filter(available=False)
            if queryset.count() == 0:
                self.error = "Aucun livre n'est indisponible."
                

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the response.
        """
        context = super().get_context_data(**kwargs)
        
        # Get total books count
        books = Book.objects.all()
        context["total_books"] = books.count()
        context["total_books_availables"] = books.filter(available=True).count()
        context["total_books_unavailables"] = books.filter(available=False).count()
        context["error"] = self.error

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request and ensures it triggers the right filtering.
        """
        # Reuse the get method for filtering logic
        return self.get(request, *args, **kwargs)

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