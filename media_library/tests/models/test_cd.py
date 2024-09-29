import pytest
from library.models import Cd


class TestCd:

    @pytest.mark.django_db
    def test_cd_creation(self):
        """
        Test the creation of a Cd object.

        Creates a Cd object, and verifies that the object has been created correctly.
        The test checks that all the attributes of the object have been assigned correctly.
        """

        cd = Cd.objects.create(
            title="Electric Ladyland",
            available=True,
            slug="electric-ladyland",
            artist="Jimi Hendrix",
        )

        # Test the attributes
        assert cd.title == "Electric Ladyland"
        assert cd.available == True
        assert cd.slug == "electric-ladyland"
        assert cd.artist == "Jimi Hendrix"

    @pytest.mark.django_db
    def test_str(self):
        """
        Test the __str__() method of the Cd model.

        Creates a Cd object, and verifies that the __str__() method returns the
        expected string, which is the title of the CD followed by the artist.
        """
        cd = Cd.objects.create(
            title="Electric Ladyland",
            artist="Jimi Hendrix",
        )

        assert str(cd) == "Electric Ladyland - Jimi Hendrix"
