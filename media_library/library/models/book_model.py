from django.db import models
from library.models.media_model import Media

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
    
    def update_book_available(book_id):
        get_book = Book.objects.get(id=book_id)
        get_book.available = not get_book.available
        get_book.save()