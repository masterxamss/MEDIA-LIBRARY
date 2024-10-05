import pytest
from library.models import Dvd


class TestDvd:
    # Test create a dvd
    @pytest.mark.django_db
    def test_dvd_creation(self):
        """
        Tests the creation of a DVD object.

        Creates a new DVD object in the database using Dvd.objects.create().
        Checks that all the fields in the DVD have been assigned correctly using assertions.
        Each assert checks that the value of the field created corresponds to what is expected.
        """
        dvd = Dvd.objects.create(
            title="A Dog's Life",
            available=True,
            slug="a-dogs-life",
            director="Charles Chaplin"
        )

        assert dvd.title == "A Dog's Life"
        assert dvd.available == True
        assert dvd.slug == "a-dogs-life"
        assert dvd.director == "Charles Chaplin"

    @pytest.mark.django_db
    def test_str(self):
        """
        Tests the __str__() method of the Dvd model.

        Creates a Dvd object, and verifies that the __str__() method returns the
        expected string, which is the title of the DVD followed by the name of the director.
        """
        dvd = Dvd.objects.create(
            title="A Dog's Life",
            director="Charles Chaplin"
        )

        assert dvd.__str__() == "DVD: A Dog's Life"
