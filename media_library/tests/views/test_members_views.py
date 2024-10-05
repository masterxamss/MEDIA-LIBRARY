import pytest
from django.urls import reverse
from library.models import Member
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestMemberViews:

    @pytest.fixture
    def authenticated_client(self, client):
        """
        Creates an authenticated user for the test.
        """
        User.objects.create_user(username='testuser', password='12345')
        client.login(username='testuser', password='12345')
        return client


    @pytest.fixture
    def members(self):
        return Member.objects.create(
            id = 1,
            first_name = 'John',
            last_name = 'Doe',
            email = 'jdoe@me.com',
            phone = '1234567890',
            blocked = False,
            street = '123 Main St',
            postal_code = '12345',
            city = 'Anytown'
        )
    
    def test_create_members_view_renders_correctly(self, client, authenticated_client):
        """
        Tests whether the create member view renders the correct template
        and returns a 200 status code.
        """
        url = reverse('create-member')
        response = client.get(url)
        assert response.status_code == 200
        assert 'library/members/member_form.html' in [t.name for t in response.templates]


    def test_create_members_success(self, client, authenticated_client):
        """
        Tests whether the creation of a member occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client to a new URL.
        """
        data = {
            'first_name':'John',
            'last_name':'Doe',
            'email':'jdoe@me.com',
            'phone':'1234567890',
            'blocked': False,
            'street':'123 Main St',
            'postal_code':'12345',
            'city':'Anytown'
        }
        url = reverse('create-member')
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse('gest-members')
        
        # Check that the member has been created
        assert Member.objects.filter(first_name='John').exists()


    def test_create_members_invalid_data(self, client, authenticated_client):
        """
        Tests whether the creation of a members with invalid data (e.g. empty title)
        occurs correctly via POST and that the user is redirected to the successful URL.
        """
        url = reverse('create-member')
        data = {
            'first_name':'',
            'last_name':'Doe',
            'email':'jdoe@me.com',
            'phone':'1234567890',
            'blocked': False,
            'street':'123 Main St',
            'postal_code':'12345',
            'city':'Anytown'
        }
        response = client.post(url, data)
        assert response.status_code == 200  # It should return to the form with errors
        
        form = response.context.get('form')
        assert form is not None
        assert form.errors  # Checks the form for errors
        assert 'first_name' in form.errors  # Check that the error is in the “name” field

        assert not Member.objects.filter(first_name='John').exists()  # Check that the members has not been created


    def test_delete_members(self, client, authenticated_client, members):
        """
        Tests whether the deletion of a member occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client (browser or other application) to a new URL.
        """
        url = reverse('delete-member' , kwargs={'id': members.id})
        response = client.post(url)
        assert response.status_code == 302
        assert response.url == reverse('gest-members')
        
        # Check that the members has been deleted
        assert not Member.objects.filter(id=members.id).exists()


    def test_delete_non_existent_members(self, authenticated_client):
        """
        Tests whether the deletion of a non-existent member returns a 404 error.
        """
        url = reverse('delete-game', kwargs={'slug': 'non-existent-members'})
        response = authenticated_client.post(url)
        assert response.status_code == 404


    def test_update_members(self, client, authenticated_client, members):
        """
        Tests whether the update of a member occurs correctly via POST
        and whether the user is redirected to the successful URL.
        """
        updated_data = {
            'first_name':'Updated Member',
            'last_name':'Doe',
            'email':'jdoe@me.com',
            'phone':'1234567890',
            'blocked': False,
            'street':'123 Main St',
            'postal_code':'12345',
            'city':'Anytown'
        }

        url = reverse('update-member' , kwargs={'id': members.id})
        response = client.post(url, updated_data)

        assert response.status_code == 302
        assert response.url == reverse('gest-members')
        
        # Check that the member has been updated
        members.refresh_from_db()
        assert  members.first_name == 'Updated Member'
