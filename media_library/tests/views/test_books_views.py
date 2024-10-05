import pytest
from django.urls import reverse
from library.models import Book
from django.forms.models import model_to_dict
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestBooksViews:

    @pytest.fixture
    def authenticated_client(self, client):
        """
        Creates an authenticated user for the test.
        """
        User.objects.create_user(username='testuser', password='12345')
        client.login(username='testuser', password='12345')
        return client


    @pytest.fixture
    def book(self):
        return Book.objects.create(
            title = 'New Book',
            author = 'Author Test',
            pages = 123,
            slug = 'newbook',
            language = 'English',
            image = 'images/book-placeholder.jpg',
            release_date = '2023-01-01',
            publisher = 'Publisher Test'
        )
    
    def test_create_book_view_renders_correctly(self, client, authenticated_client):
        """
        Tests whether the create book view renders the correct template
        and returns a 200 status code.
        """
        url = reverse('create-book')
        response = client.get(url)
        assert response.status_code == 200
        assert 'library/books/book_form.html' in [t.name for t in response.templates]


    def test_create_book_success(self, client, authenticated_client, book):
        """
        Tests whether the creation of a book occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client to a new URL.
        """
        data = {
            'title': 'Unique Book Title',
            'author': 'Autor Teste',
            'pages': 123,
            'language': 'English',
            'release_date': '2023-01-01',
            'publisher': 'Publisher Test'
        }
        url = reverse('create-book')
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse('gest-books')
        
        # Check that the book has been created
        assert Book.objects.filter(title='New Book').exists()


    def test_create_book_invalid_data(self, client, authenticated_client):
        """
        Tests whether the creation of a book with invalid data (e.g. empty title)
        occurs correctly via POST and that the user is redirected to the successful URL.
        """
        url = reverse('create-book')
        data = {
            'title': '',  # Invalid title (required field empty)
            'author': 'Autor Teste',
            'pages': 123,
            'language': 'Portuguese',
            'release_date': '2023-01-01',
            'publisher': 'Publisher Test'
        }
        response = client.post(url, data)
        assert response.status_code == 200  # It should return to the form with errors
        
        form = response.context.get('form')
        assert form is not None
        assert form.errors  # Checks the form for errors
        assert 'title' in form.errors  # Check that the error is in the “title” field

        assert not Book.objects.filter(author='Autor Teste').exists()  # Check that the book has not been created


    def test_delete_book(self, client, authenticated_client, book):
        """
        Tests whether the deletion of a book occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client (browser or other application) to a new URL.
        """
        url = reverse('book-delete' , kwargs={'slug': book.slug})
        response = client.post(url)
        assert response.status_code == 302
        assert response.url == reverse('gest-books')
        
        # Check that the book has been deleted
        assert not Book.objects.filter(slug=book.slug).exists()


    def test_delete_non_existent_book(self, authenticated_client):
        """
        Tests whether the deletion of a non-existent book returns a 404 error.
        """
        url = reverse('book-delete', kwargs={'slug': 'non-existent-book'})
        response = authenticated_client.post(url)
        assert response.status_code == 404


    def test_update_book(self, client, authenticated_client, book):
        """
        Tests whether the update of a book occurs correctly via POST
        and whether the user is redirected to the successful URL.
        """
        updated_data = {
            'title': 'Updated Book',
            'author': 'Autor Teste',
            'pages': 123,
            'language': 'English',
            'release_date': '2023-01-01',
            'publisher': 'Publisher Test'
        }

        url = reverse('book-update' , kwargs={'slug': book.slug})
        response = client.post(url, updated_data)
        assert response.status_code == 302
        assert response.url == reverse('gest-books')
        
        # Check that the book has been updated
        book.refresh_from_db()
        assert  book.title == 'Updated Book'



























#     @pytest.fixture
#     def create_books(self):
#         """
#         Pytest fixture that creates 3 test books for testing the view that displays all books.
#         """   
#         Book.objects.create(
#             title='Book A',
#             slug='book-a',
#             author='Author A',
#             pages=100,
#             language='English',
#             release_date=date(2020, 1, 1),
#             publisher='Publisher A'
#         )
#         Book.objects.create(
#             title='Book B',
#             slug='book-b',
#             author='Author B',
#             pages=100,
#             language='English',
#             release_date=date(2020, 1, 1),
#             publisher='Publisher B'
#         )
#         Book.objects.create(
#             title='Book C',
#             slug='book-c',
#             author='Author C',
#             pages=100,
#             language='English',
#             release_date=date(2020, 1, 1),
#             publisher='Publisher C'
#         )

#     def test_view_status_code(self, client, create_books):
#         """
#         Tests that the view returns a 200 status code when a GET request is sent to it.
#         """
#         response = client.get('/books/')
#         assert response.status_code == 200


#     def test_view_uses_correct_template(self, client, create_books):
#         """
#         Tests that the view uses the correct template.

#         The test first sends a GET request to the view.
#         Then it verifies that the response status code is 200.
#         Finally, it verifies that the response templates include the 'member/books.html' template.
#         """
#         response = client.get(reverse('gest-books'))
#         assert response.status_code == 200
#         assert 'library/books/gest_books.html' in [t.name for t in response.templates]


#     def test_view_returns_correct_books(self, client, create_books):
#         """
#         Tests that the view returns all books in the database.

#         The test first sends a GET request to the view.
#         Then it verifies that the response status code is 200.
#         Finally, it verifies that the response contains a list of all books in the database, with the books in the correct order.
#         """
#         response = client.get(reverse('books'))
#         assert response.status_code == 200
#         books = response.context['books']
#         assert len(books) == 3
#         assert books[0].title == 'Book A'
#         assert books[1].title == 'Book B'
#         assert books[2].title == 'Book C'


# @pytest.mark.django_db
# class TestBookDetailView:

#     @pytest.fixture
#     def create_book(self, db):
#         """
#         Pytest fixture that creates a test book for testing the view that displays a single book.
#         """
#         return Book.objects.create(
#             title='Book A',
#             slug='book-a',
#             author='Author A',
#             pages=100,
#             language='English',
#             release_date=date(2020, 1, 1), 
#             publisher='Publisher A'
#         )


#     def test_book_detail_view_status_code(self, client, create_book):
#         """
#         Tests that the book detail view returns a 200 status code when a GET request is sent to it.
#         """
#         response = client.get(
#             reverse('gest-book-detail', kwargs={'slug': create_book.slug}))
#         assert response.status_code == 200


#     def test_book_detail_uses_correct_template(self, client, create_book):
#         """
#         Tests that the book detail view uses the correct template.

#         The test first sends a GET request to the view.
#         Then it verifies that the response status code is 200.
#         Finally, it verifies that the response templates include the 'member/media_detail.html' template.
#         """
#         response = client.get(
#             reverse('gest-book-detail', kwargs={'slug': create_book.slug}))
#         assert response.status_code == 200
#         assert 'library/gest_media.html' in [
#             t.name for t in response.templates]


#     def test_book_detail_returns_correct_book(self, client, create_book):
#         """
#         Tests that the book detail view returns the correct book when a GET request is sent to it.

#         The test first sends a GET request to the view.
#         Then it verifies that the response status code is 200.
#         Finally, it verifies that the response contains the correct book.
#         """
#         response = client.get(
#             reverse('gest-book-detail', kwargs={'slug': create_book.slug}))
#         assert response.status_code == 200
#         book_detail = response.context['book_detail']
#         assert book_detail.title == 'Book A'
#         assert book_detail.slug == 'book-a'
#         assert book_detail.author == 'Author A'
#         assert book_detail.pages == 100
#         assert book_detail.language == 'English'
#         assert book_detail.release_date == date(2020, 1, 1)
#         assert book_detail.publisher == 'Publisher A'
