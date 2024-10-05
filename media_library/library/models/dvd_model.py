from django.db import models
from library.models.media_model import Media
from django.core.validators import MaxValueValidator, MinValueValidator


class Dvd(Media):
    director = models.CharField(max_length=255, null=False, blank=True)
    year = models.IntegerField(default=0, null=False, blank=True)
    writer = models.CharField(
        max_length=255, default="", null=False, blank=True)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], default=0, null=True,
        blank=True
    )
    category = models.CharField(
        max_length=150, default="", null=False, blank=True)

    def __str__(self):
        return f'DVD: {self.title}'

    def update_dvd_available(dvd_id):
        """
        Toggles the availability of a DVD.

        Args:
            dvd_id (int): The id of the DVD to update.
        """
        get_dvd = Dvd.objects.get(id=dvd_id)
        get_dvd.available = not get_dvd.available
        get_dvd.save()
