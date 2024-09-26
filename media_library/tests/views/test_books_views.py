import pytest
from django.urls import reverse
from library.models import Book
from datetime import date


@pytest.mark.django_db
class TestBooksView:

    @pytest.fixture
    def create_books(self):
        """
        Pytest fixture that creates 3 test books for testing the view that displays all books.
        """   
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

    def test_view_status_code(self, client, create_books):
        """
        Tests that the view returns a 200 status code when a GET request is sent to it.
        """
        response = client.get('/books/')
        assert response.status_code == 200


    def test_view_uses_correct_template(self, client, create_books):
        """
        Tests that the view uses the correct template.

        The test first sends a GET request to the view.
        Then it verifies that the response status code is 200.
        Finally, it verifies that the response templates include the 'member/books.html' template.
        """
        response = client.get(reverse('books'))
        assert response.status_code == 200
        assert 'member/books.html' in [t.name for t in response.templates]


    def test_view_returns_correct_books(self, client, create_books):
        """
        Tests that the view returns all books in the database.

        The test first sends a GET request to the view.
        Then it verifies that the response status code is 200.
        Finally, it verifies that the response contains a list of all books in the database, with the books in the correct order.
        """
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
        """
        Pytest fixture that creates a test book for testing the view that displays a single book.
        """
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
        """
        Tests that the book detail view returns a 200 status code when a GET request is sent to it.
        """
        response = client.get(
            reverse('book_detail', kwargs={'slug': create_book.slug}))
        assert response.status_code == 200


    def test_book_detail_uses_correct_template(self, client, create_book):
        """
        Tests that the book detail view uses the correct template.

        The test first sends a GET request to the view.
        Then it verifies that the response status code is 200.
        Finally, it verifies that the response templates include the 'member/media_detail.html' template.
        """
        response = client.get(
            reverse('book_detail', kwargs={'slug': create_book.slug}))
        assert response.status_code == 200
        assert 'member/media_detail.html' in [
            t.name for t in response.templates]


    def test_book_detail_returns_correct_book(self, client, create_book):
        """
        Tests that the book detail view returns the correct book when a GET request is sent to it.

        The test first sends a GET request to the view.
        Then it verifies that the response status code is 200.
        Finally, it verifies that the response contains the correct book.
        """
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
