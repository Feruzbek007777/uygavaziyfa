from django.contrib import admin
from .models import Genre, Books


admin.site.register(Books)
admin.site.register(Genre)