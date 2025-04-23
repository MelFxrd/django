from django.contrib import admin
from products.models import Author, Book

admin.site.register(Book)
admin.site.register(Author)
