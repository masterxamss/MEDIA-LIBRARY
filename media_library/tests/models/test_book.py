import pytest
from library.models import Book


class TestBook():

    @pytest.mark.django_db
    def test_book_creation(self):
        """
        Tests the creation of a Book object.

        Creates a new Book object in the database using Book.objects.create().
        Checks that all the fields in the book have been assigned correctly using assertions.
        Each assert checks that the value of the field created corresponds to what is expected.
        """
        book = Book.objects.create(
            title="Lord of the Rings",
            available=True,
            slug="lord-of-the-rings",
            author="J. R. R. Tolkien",
            pages=1000,
            language="English",
            release_date="2001-01-01",
            publisher="Houghton Mifflin",
            image=""
        )

        assert book.title == "Lord of the Rings"
        assert book.available == True
        assert book.slug == "lord-of-the-rings"
        assert book.author == "J. R. R. Tolkien"
        assert book.pages == 1000
        assert book.language == "English"
        assert book.release_date == "2001-01-01"
        assert book.publisher == "Houghton Mifflin"
        assert book.image == ""

    @pytest.mark.django_db
    def test_str(self):
        """
        Tests the __str__() method of the Book model.

        Creates a Book object, and verifies that the __str__() method returns the
        expected string, which is the title of the book followed by the name of the author.
        """
        book = Book.objects.create(
            title="Lord of the Rings",
            available=True,
            slug="lord-of-the-rings",
            author="J. R. R. Tolkien",
            pages=1000,
            language="English",
            release_date="2001-01-01",
            publisher="Houghton Mifflin",
            image=""
        )

        assert str(book) == "Lord of the Rings - J. R. R. Tolkien"
