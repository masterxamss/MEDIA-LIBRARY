import pytest
from django.urls import reverse
from library.models import Cd
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestCdsViews:

    @pytest.fixture
    def authenticated_client(self, client):
        """
        Creates an authenticated user for the test.
        """
        User.objects.create_user(username='testuser', password='12345')
        client.login(username='testuser', password='12345')
        return client


    @pytest.fixture
    def cd(self):
        return Cd.objects.create(
            title = 'New Cd',
            available = True,
            slug = 'newcd',
            image = 'images/cd-placeholder.jpg',
            artist = 'Artist Test',
            album = 'Album Test',
            year = 2023,
            genre = 'Genre Test',
        )
    
    def test_create_cd_view_renders_correctly(self, client, authenticated_client):
        """
        Tests whether the create cd view renders the correct template
        and returns a 200 status code.
        """
        url = reverse('create-cd')
        response = client.get(url)
        assert response.status_code == 200
        assert 'library/cds/cd_form.html' in [t.name for t in response.templates]


    def test_create_cd_success(self, client, authenticated_client):
        """
        Tests whether the creation of a cd occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client to a new URL.
        """
        data = {
            'title':'New Cd',
            'available':True,
            'slug':'newcd',
            'image':'images/cd-placeholder.jpg',
            'artist':'Artist Test',
            'album':'Album Test',
            'year':2023,
            'genre':'Genre Test'
        }
        url = reverse('create-cd')
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse('gest-cds')
        
        # Check that the cd has been created
        assert Cd.objects.filter(title='New Cd').exists()


    def test_create_cd_invalid_data(self, client, authenticated_client):
        """
        Tests whether the creation of a cd with invalid data (e.g. empty title)
        occurs correctly via POST and that the user is redirected to the successful URL.
        """
        url = reverse('create-cd')
        data = {
            'title':'',
            'available':True,
            'slug':'newcd',
            'image':'images/cd-placeholder.jpg',
            'artist':'Artist Test',
            'album':'Album Test',
            'year':2023,
            'genre':'Genre Test'
        }
        response = client.post(url, data)
        assert response.status_code == 200  # It should return to the form with errors
        
        form = response.context.get('form')
        assert form is not None
        assert form.errors  # Checks the form for errors
        assert 'title' in form.errors  # Check that the error is in the “title” field

        assert not Cd.objects.filter(artist='Artist Test').exists()  # Check that the cd has not been created


    def test_delete_cd(self, client, authenticated_client, cd):
        """
        Tests whether the deletion of a cd occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client (browser or other application) to a new URL.
        """
        url = reverse('delete-cd' , kwargs={'slug': cd.slug})
        response = client.post(url)
        assert response.status_code == 302
        assert response.url == reverse('gest-cds')
        
        # Check that the cd has been deleted
        assert not Cd.objects.filter(slug=cd.slug).exists()


    def test_delete_non_existent_cd(self, authenticated_client):
        """
        Tests whether the deletion of a non-existent cd returns a 404 error.
        """
        url = reverse('delete-cd', kwargs={'slug': 'non-existent-cd'})
        response = authenticated_client.post(url)
        assert response.status_code == 404


    def test_update_cd(self, client, authenticated_client, cd):
        """
        Tests whether the update of a cd occurs correctly via POST
        and whether the user is redirected to the successful URL.
        """
        updated_data = {
            'title':'Updated Cd',
            'available':True,
            'slug':'newcd',
            'image':'images/cd-placeholder.jpg',
            'artist':'Artist Test',
            'album':'Album Test',
            'year':2023,
            'genre':'Genre Test'
        }

        url = reverse('update-cd' , kwargs={'slug': cd.slug})
        response = client.post(url, updated_data)
        assert response.status_code == 302
        assert response.url == reverse('gest-cds')
        
        # Check that the cd has been updated
        cd.refresh_from_db()
        assert  cd.title == 'Updated Cd'
