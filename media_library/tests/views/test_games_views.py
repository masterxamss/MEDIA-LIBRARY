import pytest
from django.urls import reverse
from library.models import BoardGame
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestBoardGamesViews:

    @pytest.fixture
    def authenticated_client(self, client):
        """
        Creates an authenticated user for the test.
        """
        User.objects.create_user(username='testuser', password='12345')
        client.login(username='testuser', password='12345')
        return client


    @pytest.fixture
    def board_game(self):
        return BoardGame.objects.create(
            name = 'New BoardGame',
            creator = 'Creator Test',
            slug = 'new-boardgame',
            image = 'images/games-placeholder.jpg',
        )
    
    def test_create_board_game_view_renders_correctly(self, client, authenticated_client):
        """
        Tests whether the create board_game view renders the correct template
        and returns a 200 status code.
        """
        url = reverse('create-game')
        response = client.get(url)
        assert response.status_code == 200
        assert 'library/board_games/board_game_form.html' in [t.name for t in response.templates]


    def test_create_board_game_success(self, client, authenticated_client):
        """
        Tests whether the creation of a board_game occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client to a new URL.
        """
        data = {
            'name':'New BoardGame',
            'creator':'Creator Test',
            'slug':'new-boardgame',
            'image':'images/board_game-placeholder.jpg',
        }
        url = reverse('create-game')
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse('gest-games')
        
        # Check that the board_game has been created
        assert BoardGame.objects.filter(name='New BoardGame').exists()


    def test_create_board_game_invalid_data(self, client, authenticated_client):
        """
        Tests whether the creation of a board_game with invalid data (e.g. empty title)
        occurs correctly via POST and that the user is redirected to the successful URL.
        """
        url = reverse('create-game')
        data = {
            'name':'',
            'creator':'Creator Test',
            'slug':'new-boardgame',
            'image':'images/board_game-placeholder.jpg',
        }
        response = client.post(url, data)
        assert response.status_code == 200  # It should return to the form with errors
        
        form = response.context.get('form')
        assert form is not None
        assert form.errors  # Checks the form for errors
        assert 'name' in form.errors  # Check that the error is in the “name” field

        assert not BoardGame.objects.filter(creator='Creator Test').exists()  # Check that the board_game has not been created


    def test_delete_board_game(self, client, authenticated_client, board_game):
        """
        Tests whether the deletion of a board_game occurs correctly via POST
        and whether the user is redirected to the successful URL.

        302 - indicates that the request was successful and that the server 
        is redirecting the client (browser or other application) to a new URL.
        """
        url = reverse('delete-game' , kwargs={'slug': board_game.slug})
        response = client.post(url)
        assert response.status_code == 302
        assert response.url == reverse('gest-games')
        
        # Check that the board_game has been deleted
        assert not BoardGame.objects.filter(slug=board_game.slug).exists()


    def test_delete_non_existent_board_game(self, authenticated_client):
        """
        Tests whether the deletion of a non-existent board_game returns a 404 error.
        """
        url = reverse('delete-game', kwargs={'slug': 'non-existent-board_game'})
        response = authenticated_client.post(url)
        assert response.status_code == 404


    def test_update_board_game(self, client, authenticated_client, board_game):
        """
        Tests whether the update of a board_game occurs correctly via POST
        and whether the user is redirected to the successful URL.
        """
        updated_data = {
            'name':'Updated BoardGame',
            'creator':'Creator Test',
            'slug':'new-boardgame',
            'image':'images/board_game-placeholder.jpg',
        }

        url = reverse('update-game' , kwargs={'slug': board_game.slug})
        response = client.post(url, updated_data)
        assert response.status_code == 302
        assert response.url == reverse('gest-games')
        
        # Check that the board_game has been updated
        board_game.refresh_from_db()
        assert  board_game.name == 'Updated BoardGame'
