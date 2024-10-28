from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
