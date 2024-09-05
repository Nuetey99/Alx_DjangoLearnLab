from django.db import models

# Create your models here.
from django.db import models

# Author model to store author's name
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model with a ForeignKey relationship to Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
