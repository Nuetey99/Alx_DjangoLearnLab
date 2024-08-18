from django.contrib import admin
from .models import Book


# Register your models here.
admin.site.register(Book)


"""
Customizing the Django Admin interface for the Book model.
- Display title, author, and publication_year in the admin list view.
- Add search functionality by title and author.
- Enable filtering by author and publication_year.
"""

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    search_fields =('title','author')
    list_filter = ('author','publication_year')

admin.site.register(Book, BookAdmin)