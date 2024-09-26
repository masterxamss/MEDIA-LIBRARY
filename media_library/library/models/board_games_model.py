from django.db import models

class BoardGame(models.Model):
    name = models.CharField(max_length=200, null=False)
    creator = models.CharField(max_length=200, null=False)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, unique=True)
    image = models.ImageField(upload_to="images", null=False, blank=True)

    def __str__(self):
        return self.name
