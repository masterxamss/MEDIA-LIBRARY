import pytest
from django.urls import reverse
from datetime import timezone, date, timedelta
from library.models import *
from django.contrib.auth.models import User
from django.forms.models import model_to_dict


@pytest.mark.django_db
class TestMediaReservationsViews:

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
            title='New Book',
            author='Author Test',
            pages=123,
            slug='newbook',
            language='English',
            image='images/book-placeholder.jpg',
            release_date='2023-01-01',
            publisher='Publisher Test'
        )


    @pytest.fixture
    def dvd(self):
        return Dvd.objects.create(
            title='New DVD',
            director='Director Test',
            year=2023,
            writer='Writer Test',
            rating=5,
            slug='newdvd',
            image='images/dvd-placeholder.jpg',
        )


    @pytest.fixture
    def cd(self):
        return Cd.objects.create(
            title='New CD',
            artist='Artist Test',
            album='Album Test',
            year=2023,
            slug='newcd',
            image='images/cd-placeholder.jpg',
        )


    @pytest.fixture
    def member(self):
        return Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jSparrow@me.com",
            phone="1234567890",
            blocked=False,
            street="123 Main St",
            postal_code="12345",
            city="Anytown"
        )


    @pytest.fixture
    def reservations(self, member, book, dvd, cd):
        return MediaReservations.objects.create(
            id=1,
            member=member,
            book=book,
            dvd=dvd,
            cd=cd,
            date_requested=date.today(),
            date_due=date.today() + timedelta(days=7),
            returned=False,
            #date_returned = ''
        )


    def test_reservations_page_renders_correctly(self, client, authenticated_client):
        """
        Tests whether the reservations page renders the correct template
        and returns a 200 status code.
        """
        url = reverse('gest-reservations')
        response = client.get(url)
        assert response.status_code == 200
        assert 'library/reservations/gest_reservations.html' in [
            template.name for template in response.templates]


    def test_filter_reservations_by_member(self, client, authenticated_client, member, reservations):
        """
        Tests whether the reservations page renders the correct template
        and returns a 200 status code when a member is searched.
        Verifies that the reservations returned contain the reservation of the searched member.
        """
        url = reverse('gest-reservations')
        data = {
            'search_member': member.first_name,
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert reservations in response.context['reservations']


    def test_filter_active_reservations(self, client, authenticated_client, reservations):
        """
        Tests whether the reservations page renders the correct template
        and returns a 200 status code when active reservations are filtered.
        Verifies that the reservations returned contain only active reservations.
        """
        reservations.returned = False
        reservations.save()

        url = reverse('gest-reservations')
        data = {
            'return_active': 'on',
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert reservations in response.context['reservations']


    def test_return_reservation(self, client, authenticated_client, reservations):
        """
        Tests whether the reservations page can mark a reservation as returned.
        Verifies that the reservation page redirects after marking a reservation as returned.
        Verifies that the reservation is marked as returned in the database.
        """
        url = reverse('gest-reservations')
        data = {
            'reservation_id': reservations.id,
        }
        response = client.post(url, data)
        assert response.status_code == 302
        reservations.refresh_from_db()
        assert reservations.returned == True


    def test_no_results_message(self, client, authenticated_client):
        """
        Tests whether the reservations page renders the correct template
        and returns a 200 status code when the search ields no results.
        Verifies that the error message is displayed in the context.
        """
        url = reverse('gest-reservations')
        data = {
            'search_member': 'nonexistent',
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert 'Aucun emprunt trouvé.' in response.context['error']


    def test_total_reservations_count(self, client, authenticated_client, reservations):
        """
        Tests whether the reservations page displays the correct count of total reservations,
        total active reservations and total completed reservations.
        """
        url = reverse('gest-reservations')
        response = client.get(url)
        assert response.context['total_reservations'] == MediaReservations.objects.count(
        )
        assert response.context['total_reservations_active'] == MediaReservations.objects.filter(
            returned=False).count()
        assert response.context['total_reservations_completed'] == MediaReservations.objects.filter(
            returned=True).count()
        

    def test_create_reservation_view_renders_correctly(self, client, authenticated_client):
    
        url = reverse('create-reservation')
        response = client.get(url)
        assert response.status_code == 200
        assert 'library/reservations/reservation_form.html' in [t.name for t in response.templates]


    def test_create_reservation_success(self, client, authenticated_client, reservations):
        data = model_to_dict(reservations)
        del data['date_returned']

        url = reverse('create-reservation')
        response = client.post(url, data)

        assert response.status_code == 302
        assert response.url == reverse('gest-reservations')
        assert MediaReservations.objects.filter(member=reservations.member).exists()


    def test_create_reservation_invalid_data(self, client, authenticated_client, reservations, member):
        """
        Tests whether the creation of a reservation with invalid data (e.g. empty member)
        occurs correctly via POST and that the user is redirected to the successful URL.
        """
        url = reverse('create-reservation')
        data = model_to_dict(reservations)
        data['member'] = ''
        del data['date_returned']

        response = client.post(url, data)
        assert response.status_code == 200
        
        form = response.context.get('form')
        assert form is not None
        assert form.errors 
        assert 'member' in form.errors 

        assert MediaReservations.objects.count() == 1


    def test_delete_reservation(self, client, authenticated_client, reservations):
        """
        Tests whether the deletion of a reservation occurs correctly via POST
        and whether the user is redirected to the successful URL.
        """
        url = reverse('delete-reservation' , kwargs={'id': reservations.id})
        response = client.post(url)
        assert response.status_code == 302
        assert response.url == reverse('gest-reservations')
        
        # Check that the reservation has been deleted
        assert not MediaReservations.objects.filter(id=reservations.id).exists()


    def test_member_blocked_for_late_return(self, client, authenticated_client, reservations, member):
        """
        Tests whether a member is blocked if a reservation is more than 7 days overdue.
        """
        reservations.date_due = date.today() - timedelta(days=8)
        reservations.save()

        url = reverse('gest-reservations')
        response = client.get(url)
        
        member.refresh_from_db()
        
        assert response.status_code == 200
        assert member.blocked is True
