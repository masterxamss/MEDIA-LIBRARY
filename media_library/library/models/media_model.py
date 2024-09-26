from django.db import models

# -----------------------------------------------------------
# MODEL MEDIA (ABSTRACT BASE MODEL)
# -----------------------------------------------------------
class Media(models.Model):
    title = models.CharField(max_length=255, null=False)
    available = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, unique=True)

    class Meta:
        abstract = True  # Does not create its own table in the database.