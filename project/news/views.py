from django.shortcuts import render
from .models import Genre, Books

def home(request):
    genres = Genre.objects.all()
    books = Books.objects.all()
    return render(request, 'index.html', {'genres' : genres, 'books' : books})


def books_by_genre(request, genre_id):
    genres = Genre.objects.all()
    books = Books.objects.filter(genre_id=genre_id)
    return render(request, 'index.html', {'genres': genres, 'books': books})


def index(request):
    genres = Genre.objects.all()
    books = Books.objects.all()
    return render(request, 'index.html', {'genres': genres, 'books': books})