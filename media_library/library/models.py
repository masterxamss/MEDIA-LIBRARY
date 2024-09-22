from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# -----------------------------------------------------------
# MODEL MEMBERS
# -----------------------------------------------------------


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
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.get_full_name()} - {self.email}'


# -----------------------------------------------------------
# MODEL BOARD GAMES
# -----------------------------------------------------------
class BoardGame(models.Model):
    name = models.CharField(max_length=200, null=False)
    creator = models.CharField(max_length=200, null=False)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, unique=True)
    image = models.ImageField(upload_to="images", null=False, blank=True)

    def __str__(self):
        return self.name


# -----------------------------------------------------------
# MODEL MEDIA (ABSTRACT BASE MODEL)
# -----------------------------------------------------------
class Media(models.Model):
    title = models.CharField(max_length=255, null=False)
    available = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, unique=True)

    class Meta:
        abstract = True  # Does not create its own table in the database.


# -----------------------------------------------------------
# MODEL BOOK INHERITING FROM ABSTRACT MEDIA
# -----------------------------------------------------------
class Book(Media):
    author = models.CharField(max_length=255, null=False)
    pages = models.IntegerField(null=False)
    language = models.CharField(max_length=50, null=False)
    release_date = models.DateField(null=False)
    publisher = models.CharField(max_length=150, null=False)
    image = models.ImageField(upload_to="images", null=False, blank=True)


    class Meta:
        verbose_name_plural = "Books"
    

    def __str__(self):
        return f'{self.title} - {self.author}'


# -----------------------------------------------------------
# MODEL DVD INHERITING FROM ABSTRACT MEDIA
# -----------------------------------------------------------
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


# -----------------------------------------------------------
# MODEL CD INHERITING FROM ABSTRACT MEDIA
# -----------------------------------------------------------
class Cd(Media):
    artist = models.CharField(max_length=255, null=False)
    album = models.CharField(max_length=255, default="", null=False, blank=True)
    year = models.IntegerField(default=0, null=False, blank=True)
    genre = models.CharField(max_length=150, default="", null=False, blank=True)
    image = models.ImageField(upload_to="images", null=False, blank=True)


    def __str__(self):
        return f'{self.title} - {self.artist}'


# -----------------------------------------------------------
# MODEL REQUESTS
# -----------------------------------------------------------
class MediaRequests(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='loans', null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='book_loans', null=True, blank=True)
    dvd = models.ForeignKey(Dvd, on_delete=models.CASCADE,
                            related_name='dvd_loans', null=True, blank=True)
    cd = models.ForeignKey(Cd, on_delete=models.CASCADE,
                           related_name='cd_loans', null=True, blank=True)
    date_requested = models.DateTimeField(default=timezone.now, null=False)
    date_due = models.DateTimeField()
    returned = models.BooleanField(default=False)
    date_returned = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Media Requests"


    def is_overdue(self):
        # Checks if the item is overdue and has not yet been returned
        if not self.returned and self.date_due < timezone.now():
            return True
        return False
    

    def return_item(self):
        # Marks the item as returned and records the return date
        if not self.returned:
            self.returned = True
            self.date_returned = timezone.now()
            self.save()

    def get_loan_duration(self):
        # Returns the total duration of the loan
        if self.returned and self.date_returned:
            return (self.date_returned - self.date_requested).days
        return None  # If it hasn't been returned yet


    def __str__(self):
        # Displays the title of the book, DVD or CD, depending on which one is filled in
        media_title = 'Livre: ' + self.book.title if self.book else 'Dvd: ' + self.dvd.title if self.dvd else 'Cd: ' +self.cd.title
        return f'{media_title} - Membre: {self.member.first_name} {self.member.last_name}'
