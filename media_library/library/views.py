from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView

from . models import Book, Cd, Dvd, BoardGame
from . forms import BookForm



def LoginView(request):
    """
    View to handle user login.

    If the request is a GET, renders a login form.
    If the request is a POST, authenticate the user and log them in.
    If the authentication fails, renders the form again with errors.
    If the form is valid, logs the user in and redirects to the homepage.
    """
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home-library'
            return redirect(next_url)
        else:
            error_message = 'Nom d\'utilisateur ou mot de passe incorrect'
    return render(request, 'library/login.html', {'error': error_message})


def LogoutView(request):
    """
    View to handle user logout.

    If the request is a GET, redirects to the login page.
    """
    if request.method == 'GET':
        logout(request)
        return redirect('login')
    # else:
    #     return redirect('home-library')


@login_required
def HomeLibraryView(request):
    """
    View to handle the homepage of the library.

    Requires the user to be logged in.

    Renders the 'library/home_library.html' template.

    :param request: the current request object
    :return: a rendered template
    """
    return render(request, 'library/home_library.html')

'''    
-----------------------------------------------------------
LIBRARY BOOKS VIEWS
-----------------------------------------------------------
'''
''' READ VIEW '''
@login_required
def LibraryBooksView(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'library/books/gest_books.html', context)

class LibraryBooksView(LoginRequiredMixin,ListView):
    template_name = "library/books/gest_books.html"
    model = Book
    ordering = ["title"]
    context_object_name = "books"
    paginate_by = 10

@login_required
def LibraryBookDetailView(request, slug):
    identified_media = get_object_or_404(Book, slug=slug)
    return render(request, "library/gest_media.html", {
        "book_detail": identified_media
    })

class LibraryBookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "library/gest_media.html"
    slug_field = 'slug'  # Especifica que o lookup será feito pelo campo slug
    slug_url_kwarg = 'slug'
    context_object_name = 'book_detail'  # Define o nome do contexto que será usado no template


''' CREATE VIEW '''

''' [FBV] - FUNCTION BASED VIEW '''
@login_required
def CreateBookView(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.slug = slugify(book.title)
            book.save()
            return redirect('gest-books')

    context = {
        'form': form,
    }
    return render(request, 'library/create_book.html', context)
''' [CBV] - CLASS BASED VIEW '''
class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books/book_form.html'
    success_url = reverse_lazy('gest-books')  # URL para redirecionar após o sucesso

    def form_valid(self, form):
        # Antes de salvar o formulário, criar o slug a partir do título
        book = form.save(commit=False)
        book.slug = slugify(book.title)
        book.save()
        return super().form_valid(form)
    

''' DELETE VIEW '''
@login_required
def BookDeleteView(request, slug):
    book = Book.objects.get(slug=slug)

    if book.method == 'POST':
        book.delete()
        return redirect('gest-books')

    context = {
        'book': book
    }
    return render(request, 'library/book_confirm_delete.html', context)

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/books/book_confirm_delete.html'
    success_url = reverse_lazy('gest-books')
    slug_field = 'slug'  # Especifica que o lookup será feito pelo campo slug
    slug_url_kwarg = 'slug'

''' UPDATE VIEW '''
@login_required
def BookUpdateView(request, slug):
    book = Book.objects.get(slug=slug)

    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('gest-books') 

    context = {
        'form': form
    }
    return render(request, 'library/book_form.html', context)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books/book_form.html'
    slug_field = 'slug'  # Especifica que o lookup será feito pelo campo slug
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-books')  # Redireciona após a atualização

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional, se necessário
        return super().form_valid(form)


# -----------------------------------------------------------
# LIBRARY CDS VIEWS
# -----------------------------------------------------------
class LibraryCdView(LoginRequiredMixin,ListView):
    template_name = "library/gest_cds.html"
    model = Cd
    ordering = ["title"]
    context_object_name = "cds"
    paginate_by = 10

@login_required
def LibraryCdDetailView(request, slug):
    identified_media = get_object_or_404(Cd, slug=slug)
    return render(request, "library/gest_media.html", {
        "cd_detail": identified_media
    })

# -----------------------------------------------------------
# LIBRARY DVDS VIEWS
# -----------------------------------------------------------
class LibraryDvdView(LoginRequiredMixin,ListView):
    template_name = "library/gest_dvds.html"
    model = Dvd
    ordering = ["title"]
    context_object_name = "dvds"
    paginate_by = 10

@login_required
def LibraryDvdDetailView(request, slug):
    identified_media = get_object_or_404(Dvd, slug=slug)
    return render(request, "library/gest_media.html", {
        "dvd_detail": identified_media
    })


# -----------------------------------------------------------
# LIBRARY BOARD GAMES VIEWS
# -----------------------------------------------------------
class LibraryBoardGamesView(LoginRequiredMixin,ListView):
    template_name = "library/gest_board_games.html"
    model = BoardGame
    ordering = ["name"]
    context_object_name = "board_games"
    paginate_by = 10

@login_required
def LibraryBoardGamesDetailView(request, slug):
    identified_media = get_object_or_404(BoardGame, slug=slug)
    return render(request, "library/gest_media.html", {
        "game_detail": identified_media
    })


