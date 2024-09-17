import pytest
from library.models import Book

class TestBook():

    @pytest.mark.django_db
    def test_book_creation(self):
        # Creation of the Book object
        book = Book.objects.create(
            title="Lord of the Rings",
            available=True,
            slug="lord-of-the-rings",
            author="J. R. R. Tolkien"
        )

        # Test the attributes
        assert book.title == "Lord of the Rings"
        assert book.available == True
        assert book.slug == "lord-of-the-rings"
        assert book.author == "J. R. R. Tolkien"


    # Test the __str__() method
    @pytest.mark.django_db
    def test_str(self):
        book = Book.objects.create(
            title="Lord of the Rings",
            author="J. R. R. Tolkien"
        )

        assert str(book) == "Lord of the Rings - J. R. R. Tolkien"