import pytest
from django.utils import timezone
from datetime import date
from library.models import Member, Book, Dvd, Cd, MediaReservations


class TestMediaRequests:

    @pytest.mark.django_db
    def test_media_request_creation_with_book(self):
        """
        Test the creation of a media request with a book.

        Creates a Member object and a Book object, and then creates a media
        request (MediaRequests) with the associated book.

        Checks the request has been created correctly and if
        the __str__() method returns the title of the book and the name of the member.
        """

        # Create a member
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jack@sparrow.com",
            phone="1234567890"
        )

        # Create a book
        book = Book.objects.create(
            title="Alice in wonderland",
            author="Lewis Carroll",
            pages=200,
            language="English",
            release_date="2001-01-01",
            publisher="Houghton Mifflin",
            image=""
        )

        # Create a media request
        media_request = MediaReservations.objects.create(
            member=member,
            book=book,
            date_due=timezone.now() + timezone.timedelta(days=7)
        )

        # Check if the media request has been created correctly
        assert media_request.member == member
        assert media_request.book == book
        assert media_request.dvd is None
        assert media_request.cd is None
        assert media_request.returned is False
        assert media_request.date_due > timezone.now()

        assert str(
            media_request) == "Livre: Alice in wonderland - Membre: Jack Sparrow"

    @pytest.mark.django_db
    def test_media_request_creation_with_dvd(self):
        """
        Test the creation of a media request with a DVD.
        """
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jack@sparrow.com",
            phone="1234567890"
        )

        dvd = Dvd.objects.create(
            title="Pirates of the Caribbean",
            director="Gore Verbinski"
        )

        media_request = MediaReservations.objects.create(
            member=member,
            dvd=dvd,
            date_due=timezone.now() + timezone.timedelta(days=7)
        )

        assert media_request.member == member
        assert media_request.book is None
        assert media_request.dvd == dvd
        assert media_request.cd is None
        assert media_request.returned is False
        assert media_request.date_due > timezone.now()

        assert str(
            media_request) == "Dvd: Pirates of the Caribbean - Membre: Jack Sparrow"

    @pytest.mark.django_db
    def test_media_request_creation_with_cd(self):
        """
        Test the creation of a media request with a CD.
        """
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jack@sparrow.com",
            phone="0987654321"
        )

        cd = Cd.objects.create(
            title="Paranoid",
            artist="Black Sabbath"
        )

        media_request = MediaReservations.objects.create(
            member=member,
            cd=cd,
            date_due=timezone.now() + timezone.timedelta(days=7)
        )

        assert media_request.member == member
        assert media_request.book is None
        assert media_request.dvd is None
        assert media_request.cd == cd
        assert media_request.returned is False
        assert media_request.date_due > timezone.now()

        assert str(media_request) == "Cd: Paranoid - Membre: Jack Sparrow"

    @pytest.mark.django_db
    def test_return_item(self):
        """
        Test the return_item() method of MediaReservations model.

        The test first creates a MediaReservations object with a future return date.
        Then it verifies that the item has not been returned.
        Then it invokes the return_item() method and verifies that the item has been returned
        and the return date has been recorded.
        Finally, it verifies that the item has been returned before the deadline.
        """
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jack@sparrow.com"
        )

        book = Book.objects.create(
            title="The Prisoner of the Caucasus",
            author="Liev Tolstói",
            pages=200,
            language="English",
            release_date="2001-01-01",
            publisher="Houghton Mifflin",
            image=""
        )

        # Creation of media order with future return date
        media_request = MediaReservations.objects.create(
            member=member,
            book=book,
            date_due=timezone.now() + timezone.timedelta(days=7),
            returned=False  # Not returned
        )

        # Ensuring that the item has not yet been returned
        assert media_request.returned == False
        assert media_request.date_returned == None

        # Invoking the return item method to mark the item as returned
        media_request.return_item()

        # Refreshing the database after the update
        media_request.refresh_from_db()

        # Verifying that the item has been returned
        assert media_request.returned == True

        # Verifying that the return date has been recorded
        assert media_request.date_returned is not None

        # Verify if the media has been returned before the deadline
        assert media_request.date_returned <= date.today()
