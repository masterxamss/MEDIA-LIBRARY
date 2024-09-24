import pytest
from django.utils import timezone
from datetime import date
from library.models import Member, Book, Dvd, Cd, MediaReservations

'''
    Test creat a media request : 

    * Creates a Member object and a Book, Cd or Dvd object, and then creates a media
    request (MediaRequests) with the associated media.

    * Checks the request has been created correctly and if
    the __str__() method returns the title of the media and the name of the member.
'''

class TestMediaRequests:
    # Method for creating a book request
    @pytest.mark.django_db
    def test_media_request_creation_with_book(self):
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

        assert str(media_request) == "Livre: Alice in wonderland - Membre: Jack Sparrow"

    # Method to create a dvd request

    @pytest.mark.django_db
    def test_media_request_creation_with_dvd(self):
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

        assert str(media_request) == "Dvd: Pirates of the Caribbean - Membre: Jack Sparrow"

    # Method to create a cd request

    @pytest.mark.django_db
    def test_media_request_creation_with_cd(self):
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

    '''
    ------------------------------------------------------------------------------------
        Test to check methodc is_overdue() that checks
        if the media has not been returned yet.

        Scenarios :

        * [ TEST-1 ]: Unreturned loan and return date in the past (overdue).
        * [ TEST-2 ]: Loan not returned and return date in the future (not overdue).
        * [ TEST-3 ]: Loan returned (no matter the date, must return False).
    ------------------------------------------------------------------------------------
    '''

    # [ TEST-1 ]
    @pytest.mark.django_db
    def test_is_overdue_with_overdue_item(self):
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jack@sparrow.com"
        )

        book = Book.objects.create(
            title="Alice in wonderland",
            author="Lewis Carroll",
            pages=200,
            language="English",
            release_date="2001-01-01",
            publisher="Houghton Mifflin",
            image="" 
        )

        # Creation of the media order with the return date in the past
        media_request = MediaReservations.objects.create(
            member=member,
            book=book,
            # Return date two days in the past
            date_due=timezone.now() - timezone.timedelta(days=2),
            returned=False
        )

        # if true, the media has not been returned yet
        assert media_request.is_overdue() == True

    # [ TEST-2 ]

    @pytest.mark.django_db
    def test_is_overdue_with_future_due_date(self):
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jack@sparrow.com"
        )

        book = Book.objects.create(
            title="Anna Karenina",
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
            date_due=timezone.now() + timezone.timedelta(days=5),  # Future return date
            returned=False
        )

        # if false, media has not yet been returned but is still within the deadline
        assert media_request.is_overdue() == False

    # [ TEST-3 ]

    @pytest.mark.django_db
    def test_is_overdue_with_returned_item(self):
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

        media_request = MediaReservations.objects.create(
            member=member,
            book=book,
            date_due=timezone.now() - timezone.timedelta(days=1),  # Date of return in the past
            returned=True  # Returned
        )

        # if false, media has been returned but out of the deadline
        assert media_request.is_overdue() == False

    '''
    -------------------------------------------------------------------------------------
        Test to check if the media has been returned and in case of yes update record
    -------------------------------------------------------------------------------------
    '''

    @pytest.mark.django_db
    def test_return_item(self):
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


    '''
    -------------------------------------------------------------------
        Test to check if the loan duration is calculated correctly

        Context :
        * Date of request: 7 days ago
        * Date of return: Current day
        * Loan duration: 7 days
    -------------------------------------------------------------------
    '''
    @pytest.mark.django_db
    def test_loan_duration(self):
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

        media_request = MediaReservations.objects.create(
            member=member,
            book=book,
            date_requested=timezone.now() - timezone.timedelta(days=7),
            date_due=timezone.now() + timezone.timedelta(days=7),
            date_returned=timezone.now(),
            returned=True
        )

        loan_duration = media_request.get_loan_duration()

        value_expected = 7

        assert loan_duration == value_expected
