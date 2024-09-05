from rest_framework import serializers
from .models import Author, Book

# BookSerializer to handle all Book fields and validate the publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# AuthorSerializer that nests the BookSerializer to dynamically serialize related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer

    class Meta:
        model = Author
        fields = ['name', 'books']