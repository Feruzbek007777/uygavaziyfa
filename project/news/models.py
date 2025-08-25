from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.title
