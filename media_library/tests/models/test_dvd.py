import pytest
from library.models import Dvd

class TestDvd:
    # Test create a dvd
    @pytest.mark.django_db
    def test_dvd_creation(self):
        # Create a dvd object
        dvd = Dvd.objects.create(
            title="A Dog's Life",
            available=True,
            slug="a-dogs-life",
            director="Charles Chaplin"
        )

        # Test the attributes
        assert dvd.title == "A Dog's Life"
        assert dvd.available == True
        assert dvd.slug == "a-dogs-life"
        assert dvd.director == "Charles Chaplin"


    # Test __str__
    @pytest.mark.django_db
    def test_str(self):
        dvd = Dvd.objects.create(
            title="A Dog's Life",
            director="Charles Chaplin"
        )

        assert dvd.__str__() == "A Dog's Life - Charles Chaplin"