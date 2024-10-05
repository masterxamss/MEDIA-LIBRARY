from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=10, null=False)
    blocked = models.BooleanField(default=False)
    street = models.CharField(max_length=100, null=False)
    postal_code = models.CharField(max_length=5, null=False)
    city = models.CharField(max_length=100, null=False)

    def get_full_name(self):
        """
        Returns the full name of a member.

        Returns:
            str: The full name of the member (first name and last name separated by a space).
        """
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        """
        Returns the full name of the member.

        Returns:
            str: The full name of the member (first name and last name separated by a space).
        """
        return f'{self.get_full_name()}'

    def get_member_blocked(member_id):
        """
        Checks if a member is blocked.

        Args:
            member_id (int): The id of the member.

        Returns:
            bool: True if the member is blocked, False otherwise.
        """
        member_bloqued = Member.objects.filter(
            id=member_id, blocked=True).exists()
        return member_bloqued
