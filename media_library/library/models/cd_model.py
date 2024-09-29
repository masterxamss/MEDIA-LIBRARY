from django.db import models
from library.models.media_model import Media

class Cd(Media):
    artist = models.CharField(max_length=255, null=False)
    album = models.CharField(max_length=255, default="", null=False, blank=True)
    year = models.IntegerField(default=0, null=False, blank=True)
    genre = models.CharField(max_length=150, default="", null=False, blank=True)
    image = models.ImageField(upload_to="images", null=False, blank=True)
    description = models.TextField(max_length=2000, null=True, default="", blank=True)


    def __str__(self):
        return f'{self.title} - {self.artist}'
    
    def update_cd_available(cd_id):
        """
        Toggles the availability of a CD.

        Args:
            cd_id (int): The id of the CD to update.
        """
        get_cd = Cd.objects.get(id=cd_id)
        get_cd.available = not get_cd.available
        get_cd.save()