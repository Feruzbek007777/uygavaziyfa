from django.shortcuts import render, get_object_or_404
from .models import Books, Genre  # sendagi model nomlari shu bo'lishi kerak

def index(request):
    genres = Genre.objects.all()
    books = Books.objects.all()
    return render(request, 'index.html', {'genres': genres, 'books': books})

def books_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genres = Genre.objects.all()
    books = Books.objects.filter(genre=genre)
    return render(request, 'index.html', {'genres': genres, 'books': books, 'selected_genre': genre})

def book_detail(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
