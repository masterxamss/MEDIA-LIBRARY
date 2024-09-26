from django.db import models
from library.models.media_model import Media
from django.core.validators import MaxValueValidator, MinValueValidator

class Dvd(Media):
    director = models.CharField(max_length=255, null=False, blank=True)
    year = models.IntegerField(default=0, null=False, blank=True)
    writer = models.CharField(max_length=255,default="", null=False, blank=True)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)],default=0, null=True,
        blank=True
    )
    category = models.CharField(max_length=150, default="", null=False, blank=True)
    description = models.TextField(max_length=500, null=True, default="", blank=True)
    image = models.ImageField(upload_to="images", null=False, blank=True)


    def __str__(self):
        return f'{self.title} - {self.director}'
    
    def update_dvd_available(dvd_id):
        get_dvd = Dvd.objects.get(id=dvd_id)
        get_dvd.available = not get_dvd.available
        get_dvd.save()