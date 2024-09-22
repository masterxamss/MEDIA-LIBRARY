import pytest
from library.models import BoardGame

class TestBoardGame:

    # Tests for the BoardGame model
    @pytest.mark.django_db
    def test_board_game_creation(self):
        # Creation of the BoardGame object
        board_game = BoardGame.objects.create(
            name="Xadrez",
            creator="Han Xin",
        )

        # Check the values
        assert board_game.name == "Xadrez"
        assert board_game.creator == "Han Xin"


    @pytest.mark.django_db
    def test_str(self):
        board_game = BoardGame.objects.create(
            name="Xadrez",
        )

        assert str(board_game) == "Xadrez"