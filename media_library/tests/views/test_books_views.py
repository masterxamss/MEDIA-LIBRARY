import pytest
from django.urls import reverse
from library.models import Book
from datetime import date


@pytest.mark.django_db
class TestBooksView:

    @pytest.fixture
    def create_books(self):
        # Create test data
        Book.objects.create(
            title='Book A',
            slug='book-a',
            author='Author A',
            pages=100,
            language='English',
            release_date=date(2020, 1, 1),
            publisher='Publisher A'
        )
        Book.objects.create(
            title='Book B',
            slug='book-b',
            author='Author B',
            pages=100,
            language='English',
            release_date=date(2020, 1, 1),
            publisher='Publisher B'
        )
        Book.objects.create(
            title='Book C',
            slug='book-c',
            author='Author C',
            pages=100,
            language='English',
            release_date=date(2020, 1, 1),
            publisher='Publisher C'
        )

    # Checks that the book listing page returns a status of 200 OK.
    def test_view_status_code(self, client, create_books):
        response = client.get('/books/')
        assert response.status_code == 200

    # Check that the correct template is being used (member/books.html).
    def test_view_uses_correct_template(self, client, create_books):
        response = client.get(reverse('books'))
        assert response.status_code == 200
        assert 'member/books.html' in [t.name for t in response.templates]

    # Check that the books are present in the context of the answer and that they are ordered correctly.
    def test_view_returns_correct_books(self, client, create_books):
        response = client.get(reverse('books'))
        assert response.status_code == 200
        books = response.context['books']
        assert len(books) == 3
        assert books[0].title == 'Book A'
        assert books[1].title == 'Book B'
        assert books[2].title == 'Book C'


@pytest.mark.django_db
class TestBookDetailView:

    @pytest.fixture
    def create_book(self, db):
        # Criando um CD de exemplo para o teste
        return Book.objects.create(
            title='Book A',
            slug='book-a',
            author='Author A',
            pages=100,
            language='English',
            release_date=date(2020, 1, 1), 
            publisher='Publisher A'
        )

    def test_book_detail_view_status_code(self, client, create_book):
        # Testando se a view de detalhe está acessível pela URL correta
        response = client.get(
            reverse('book_detail', kwargs={'slug': create_book.slug}))
        assert response.status_code == 200

    def test_book_detail_uses_correct_template(self, client, create_book):
        # Testando se a view usa o template correto
        response = client.get(
            reverse('book_detail', kwargs={'slug': create_book.slug}))
        assert response.status_code == 200
        assert 'member/media_detail.html' in [
            t.name for t in response.templates]

    def test_book_detail_returns_correct_book(self, client, create_book):
        # Testando se o contexto contém o CD correto
        response = client.get(
            reverse('book_detail', kwargs={'slug': create_book.slug}))
        assert response.status_code == 200
        book_detail = response.context['book_detail']
        assert book_detail.title == 'Book A'
        assert book_detail.slug == 'book-a'
        assert book_detail.author == 'Author A'
        assert book_detail.pages == 100
        assert book_detail.language == 'English'
        assert book_detail.release_date == date(2020, 1, 1)
        assert book_detail.publisher == 'Publisher A'
