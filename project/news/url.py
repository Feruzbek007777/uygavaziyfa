from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<int:genre_id>/', views.books_by_genre, name='books_by_genre'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
