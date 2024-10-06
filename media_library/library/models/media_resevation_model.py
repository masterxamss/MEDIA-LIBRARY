from django.db import models
from django.utils import timezone
from datetime import date
from library.models import Book
from library.models import Dvd
from library.models import Cd
from library.models import Member


class MediaReservations(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='loans', null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='book_loans', null=True, blank=True)
    dvd = models.ForeignKey(Dvd, on_delete=models.CASCADE,
                            related_name='dvd_loans', null=True, blank=True)
    cd = models.ForeignKey(Cd, on_delete=models.CASCADE,
                           related_name='cd_loans', null=True, blank=True)
    date_requested = models.DateField(default=date.today, null=False)
    date_due = models.DateField(
        default=date.today() + timezone.timedelta(days=7))
    returned = models.BooleanField(default=False)
    date_returned = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Media Reservations"

    def get_media_items(self):
        """
        Returns a list of media items for the reservation.
        This can be one of either a book, DVD or CD.
        """
        media_items = []
        if self.book:
            media_items.append(self.book)
        if self.dvd:
            media_items.append(self.dvd)
        if self.cd:
            media_items.append(self.cd)
        return media_items

    def return_item(self):
        """
        Marks the item as returned and records the return date.
        Sets the returned boolean to True and sets the date_returned to the current date.
        Only does this if the reservation is not already marked as returned.
        """
        if not self.returned:
            self.returned = True
            self.date_returned = date.today()
            self.save()

    def __str__(self):
        """
        Displays the title of the book, DVD or CD, depending on which one is filled in, 
        followed by the name of the member.
        """
        media_title = 'Livre: ' + self.book.title if self.book else 'Dvd: ' + \
            self.dvd.title if self.dvd else 'Cd: ' + self.cd.title
        return f'{media_title} - Membre: {self.member.first_name} {self.member.last_name}'

    def get_active_reservations(member_id):
        """
        Counts the number of active reservations for a given member.
        Args:
            member_id (int): The id of the member.
        Returns:
            int: The number of active reservations for the given member.
        """
        active_reservations = MediaReservations.objects.filter(
            member_id=member_id, returned=False).count()
        return active_reservations
    
    def is_late(self):
        """
        Checks if the reservation is late by more than 7 days.
        
        If the reservation is not returned and the current date is more than 7 days
        past the due date, sets the member's blocked attribute to True and saves the
        member. Returns True if the reservation is late and False otherwise.
        """
        if not self.returned and (timezone.now().date() - self.date_due).days > 7:
            self.member.blocked = True
            self.member.save()
            return True
        return False