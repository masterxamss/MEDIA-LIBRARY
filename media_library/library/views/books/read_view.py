from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import Book


class BooksView(ListView):
    template_name = "library/books/gest_books.html"
    model = Book
    ordering = ["title"]
    paginate_by = 10
    context_object_name = "books"

    error = None

    def get_queryset(self):
        """
        Override the default queryset to apply filtering based on the POST request.

        Retrieves the books from the database and applies the filters based on
        the POST request. If the search_title field is not empty, filters the
        books by the search_title field. If the return_availables field is
        checked, filters the books by those that are available. If the
        return_unavailables field is checked, filters the books by those that are
        not available. If the search returns no results, sets the error attribute
        of the view instance to the appropriate error message.

        Returns:
            QuerySet: The filtered queryset of books.
        """
        queryset = super().get_queryset()
        
        # Get POST parameters if any
        search_title = self.request.POST.get('search_title','').strip()
        return_availables = self.request.POST.get('return_availables')
        return_unavailables = self.request.POST.get('return_unavailables')

        # Apply filters based on POST data
        if search_title:
            queryset = queryset.filter(title__icontains=search_title)
            if queryset.count() == 0:
                self.error = "Aucun livre ne correspond à votre recherche."

        if return_availables:
            queryset = queryset.filter(available=True)
            if queryset.count() == 0:
                self.error = "Aucun livre n'est disponible."

        if return_unavailables:
            queryset = queryset.filter(available=False)
            if queryset.count() == 0:
                self.error = "Aucun livre n'est indisponible."
                

        return queryset

    def get_context_data(self, **kwargs):    
        """
        Adds additional context to the response.

        Adds the error message if any, total books, total available books,
        total unavailable books, and the status of the filters and sorting options.

        Returns:
            dict: The context as a dictionary.
        """
        context = super().get_context_data(**kwargs)
        
        # Get total books count
        books = Book.objects.all()
        context["total"] = books.count()
        context["total_availables"] = books.filter(available=True).count()
        context["total_unavailables"] = books.filter(available=False).count()
        context["error"] = self.error
        context["return_all"] = 'checked' if self.request.POST.get('return_all') else ''
        context["return_availables"] = 'checked' if self.request.POST.get('return_availables') else ''
        context["return_unavailables"] = 'checked' if self.request.POST.get('return_unavailables') else ''
        context["user"] = self.request.user

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to filter books.

        Reuses the get method for filtering logic.
        """
        return self.get(request, *args, **kwargs)

class BookDetailView(DetailView):
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