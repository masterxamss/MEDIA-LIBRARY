from django.contrib import admin
from .models import Member, BoardGame, Book, Cd, Dvd, MediaRequests

# USERNAME : Admin
# PASSWORD : 3#__45aPgG*89

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'phone', 'street', 'postal_code', 'city', 'blocked']
    list_filter = ['blocked']
    search_fields = ['first_name', 'last_name', 'email',
                     'phone', 'street', 'postal_code', 'city']


class BoardGameAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator']
    search_fields = ['name', 'creator']
    prepopulated_fields = {"slug": ("name",)}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'author', 'language', 'release_date', 'publisher']
    search_fields = ['title', 'author']


class CdAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'artist','album','year','genre']
    search_fields = ['title', 'artist']


class DvdAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'director', 'year', 'writer', 'rating', 'category', 'description']
    search_fields = ['title', 'director']


class MediaRequestsAdmin(admin.ModelAdmin):
    list_display = ['member', 'book', 'dvd', 'cd','date_requested', 'date_due', 'returned', 'date_returned']
    search_fields = ['member', 'book', 'dvd', 'cd']


admin.site.register(Member, MemberAdmin)
admin.site.register(BoardGame, BoardGameAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Cd, CdAdmin)
admin.site.register(Dvd, DvdAdmin)
admin.site.register(MediaRequests, MediaRequestsAdmin)
