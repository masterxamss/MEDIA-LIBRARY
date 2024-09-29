import pytest
from library.models import BoardGame


class TestBoardGame:
    @pytest.mark.django_db
    def test_board_game_creation(self):
        # Creation of the BoardGame object
        """
        Tests the creation of a BoardGame object.

        Creates a new BoardGame object in the database using BoardGame.objects.create().
        Checks that all the fields in the board game have been assigned correctly using assertions.
        Each assert checks that the value of the field created corresponds to what is expected.
        """
        board_game = BoardGame.objects.create(
            name="Xadrez",
            creator="Han Xin",
        )

        # Check the values
        assert board_game.name == "Xadrez"
        assert board_game.creator == "Han Xin"

    @pytest.mark.django_db
    def test_str(self):
        """
        Tests the __str__() method of the BoardGame model.

        Creates a BoardGame object, and verifies that the __str__() method returns the
        expected string, which is the name of the board game.
        """
        board_game = BoardGame.objects.create(
            name="Xadrez",
        )

        assert str(board_game) == "Xadrez"
