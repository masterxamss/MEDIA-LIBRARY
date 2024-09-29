import pytest
from library.models import Member

'''
* Test the creation of a member in the database.

* Creates a new Member object in the database using Member.objects.create().
* Checks that all the fields in the member have been assigned correctly using assertions.
* Each assert checks that the value of the field created corresponds to what is expected.

-------------------------------------------------------------------------------------------

The decorator (@pytest.mark.django_db) ensures that the test has access to a temporary,
clean database, which will be created and destroyed automatically
by Django/pytest at the start and end of the test, respectively
'''
class TestMemberCreation:
    @pytest.mark.django_db
    def test_member_creation(self):
        '''
        Tests the creation of a Member object.

        Creates a new Member object in the database using Member.objects.create().
        Checks that all the fields in the member have been assigned correctly using assertions.
        Each assert checks that the value of the field created corresponds to what is expected.
        '''
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jSparrow@me.com",
            phone="1234567890",
            blocked=False,
            street="123 Main St",
            postal_code="12345",
            city="Anytown"
        )

        assert member.first_name == "Jack"
        assert member.last_name == "Sparrow"
        assert member.email == "jSparrow@me.com"
        assert member.phone == "1234567890"
        assert member.blocked == False
        assert member.street == "123 Main St"
        assert member.postal_code == "12345"
        assert member.city == "Anytown"

    @pytest.mark.django_db
    def test_get_full_name(self):
        '''
        Tests the get_full_name() method of the Member model.

        Creates a Member object, and verifies that the get_full_name() method returns the
        expected string, which is the first name followed by the last name.
        '''
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow"
        )

        assert member.get_full_name() == "Jack Sparrow"


    @pytest.mark.django_db
    def test_str(self):
        '''
        Tests the __str__() method of the Member model.

        Creates a Member object, and verifies that the __str__() method returns the
        expected string, which is the first name followed by the last name.
        '''
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jSparrow@me.com"
        )

        assert str(member) == "Jack Sparrow"

