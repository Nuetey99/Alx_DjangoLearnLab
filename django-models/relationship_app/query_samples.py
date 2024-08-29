from .models import Author, Book, Library, Librarian
from django.shortcuts import render

# Prepare a Python script query_samples.py in the relationship_app directory. 
# This script should contain the query for each of the following of relationship:
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def all_books_in_a_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    books.all()
    return books

def librarian(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian