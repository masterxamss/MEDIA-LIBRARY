import pytest
from django.urls import reverse
from library.models import Dvd
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestDvdsViews:

    @pytest.fixture
    def authenticated_client(self, client):
        """
        Creates an authenticated user for the test.
        """
        User.objects.create_user(username='testuser', password='12345')
        client.login(username='testuser', password='12345')
        return client


    @pytest.fixture
    def dvd(self):
        return Dvd.objects.create(
            title = 'New Dvd',
            available = True,
            director = 'Director Test',
            year = 2023,
            writer = 'Writer Test',
            rating = 5,
            slug = 'newdvd',
            image = 'images/dvd-placeholder.jpg',
        )
    
    def test_create_dvd_view_renders_correctly(self, client, authenticated_client):
        """
        Tests whether the create dvd view renders the correct template
        and returns a 200 status code.
        """
        url = reverse('create-dvd')
        response = client.get(url)
        assert response.status_code == 200
        assert 'library/dvds/dvd_form.html' in [t.name for t in response.templates]


    def test_create_dvd_success(self, client, authenticated_client):
        """
        Tests whether the creation of a dvd occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client to a new URL.
        """
        data = {
            'title':'Unique Dvd',
            'available':'True',
            'director':'Director Test',
            'year': 2023,
            'writer':'Writer Test',
            'rating':5,
            'slug':'unique-dvd',
            'image':'images/dvd-placeholder.jpg'
        }
        url = reverse('create-dvd')
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse('gest-dvds')
        
        # Check that the dvd has been created
        assert Dvd.objects.filter(title='Unique Dvd').exists()


    def test_create_dvd_invalid_data(self, client, authenticated_client):
        """
        Tests whether the creation of a dvd with invalid data (e.g. empty title)
        occurs correctly via POST and that the user is redirected to the successful URL.
        """
        url = reverse('create-dvd')
        data = {
            'title':'',
            'available':'True',
            'director':'Director Test',
            'year': 2023,
            'writer':'Writer Test',
            'rating':5,
            'slug':'unique-dvd',
            'image':'images/dvd-placeholder.jpg'
        }
        response = client.post(url, data)
        assert response.status_code == 200  # It should return to the form with errors
        
        form = response.context.get('form')
        assert form is not None
        assert form.errors  # Checks the form for errors
        assert 'title' in form.errors  # Check that the error is in the “title” field

        assert not Dvd.objects.filter(director='Director Test').exists()  # Check that the dvd has not been created


    def test_delete_dvd(self, client, authenticated_client, dvd):
        """
        Tests whether the deletion of a dvd occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client (browser or other application) to a new URL.
        """
        url = reverse('delete-dvd' , kwargs={'slug': dvd.slug})
        response = client.post(url)
        assert response.status_code == 302
        assert response.url == reverse('gest-dvds')
        
        # Check that the dvd has been deleted
        assert not Dvd.objects.filter(slug=dvd.slug).exists()


    def test_delete_non_existent_dvd(self, authenticated_client):
        """
        Tests whether the deletion of a non-existent dvd returns a 404 error.
        """
        url = reverse('delete-dvd', kwargs={'slug': 'non-existent-dvd'})
        response = authenticated_client.post(url)
        assert response.status_code == 404


    def test_update_dvd(self, client, authenticated_client, dvd):
        """
        Tests whether the update of a dvd occurs correctly via POST
        and whether the user is redirected to the successful URL.
        """
        updated_data = {
            'title':'Updated dvd',
            'available':'True',
            'director':'Director Test',
            'year': 2023,
            'writer':'Writer Test',
            'rating':5,
            'slug':'unique-dvd',
            'image':'images/dvd-placeholder.jpg'
        }

        url = reverse('update-dvd' , kwargs={'slug': dvd.slug})
        response = client.post(url, updated_data)
        assert response.status_code == 302
        assert response.url == reverse('gest-dvds')
        
        # Check that the dvd has been updated
        dvd.refresh_from_db()
        assert  dvd.title == 'Updated dvd'
