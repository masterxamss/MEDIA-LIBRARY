from django.db import models


class Media(models.Model):
    title = models.CharField(max_length=255, null=False)
    available = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False,
                            blank=True, db_index=True, unique=True)
    image = models.ImageField(upload_to="images", null=False, blank=True)
    description = models.TextField(
        max_length=2000, null=True, default="", blank=True)

    class Meta:
        abstract = True  # Does not create its own table in the database.
