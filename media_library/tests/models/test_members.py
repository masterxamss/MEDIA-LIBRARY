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


    '''
    * Verify that the get_full_name method works correctly.

    * Create a Member object with first_name and last_name.
    * Use the get_full_name() method to return the full name.
    * Check, using assert, that the value returned is “Jack Sparrow”.
    '''
    @pytest.mark.django_db
    def test_get_full_name(self):
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow"
        )

        assert member.get_full_name() == "Jack Sparrow"

    '''
    * Check whether Member's __str__() method returns the expected string.

    * Creates a Member object with first_name, last_name and email.
    * Use the str() function to convert the object into a string.
    * Check, with assert, that the string returned is “Jack Sparrow jSparrow@me.com”.
    '''

    @pytest.mark.django_db
    def test_str(self):
        member = Member.objects.create(
            first_name="Jack",
            last_name="Sparrow",
            email="jSparrow@me.com"
        )

        assert str(member) == "Jack Sparrow - jSparrow@me.com"

