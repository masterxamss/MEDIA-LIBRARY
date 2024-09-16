from django.db import models
from django.utils import timezone

# Create your models here.

#-----------------------------------------------------------
# MODEL MEMBERS
#-----------------------------------------------------------
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
        return f'{self.get_full_name()} {self.email}'


#-----------------------------------------------------------    
# MODEL BOARD GAMES
#-----------------------------------------------------------
class BoardGame(models.Model):
    name = models.CharField(max_length=200, null=False)
    creator = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name    


#-----------------------------------------------------------
# MODEL MEDIA (ABSTRACT BASE MODEL)
#-----------------------------------------------------------
class Media(models.Model):
    title = models.CharField(max_length=255, null=False)
    available = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)

    class Meta:
        abstract = True # Does not create its own table in the database.
        
    def __str__(self):
        return {self.title}


#-----------------------------------------------------------
# MODEL BOOK INHERITING FROM ABSTRACT MEDIA
#-----------------------------------------------------------
class Book(Media):
    author = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.title} {self.author}'
    

#-----------------------------------------------------------
# MODEL DVD INHERITING FROM ABSTRACT MEDIA
#-----------------------------------------------------------
class Dvd(Media):
    director = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.title} {self.director}'


#-----------------------------------------------------------
# MODEL CD INHERITING FROM ABSTRACT MEDIA
#-----------------------------------------------------------
class Cd(Media):
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.title} {self.artist}'


#-----------------------------------------------------------
# MODEL REQUESTS
#-----------------------------------------------------------
class Requests(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loans', null=False)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_loans', null=True, blank=True)
    dvd = models.ForeignKey('Dvd', on_delete=models.CASCADE, related_name='dvd_loans', null=True, blank=True)
    cd = models.ForeignKey('Cd', on_delete=models.CASCADE, related_name='cd_loans', null=True, blank=True)
    date_requested = models.DateTimeField(default=timezone.now, null=False)
    date_due = models.DateTimeField()
    returned = models.BooleanField(default=False)
    date_returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # Displays the title of the book, DVD or CD, depending on which one is filled in
        media_title = self.book.title if self.book else self.dvd.title if self.dvd else self.cd.title
        return f'{media_title} {self.member.first_name} {self.member.last_name}'
