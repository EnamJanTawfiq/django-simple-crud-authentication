from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'published_date', 'isbn_number']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True,read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'books']

   