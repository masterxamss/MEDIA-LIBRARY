import pytest
from library.models import Cd

class TestCd:

    # Test the creation of the Cd object
    @pytest.mark.django_db
    def test_cd_creation(self):
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


    # Test the __str__() method
    @pytest.mark.django_db
    def test_str(self):
        cd = Cd.objects.create(
            title="Electric Ladyland",
            artist="Jimi Hendrix",
        )

        assert str(cd) == "Electric Ladyland - Jimi Hendrix"