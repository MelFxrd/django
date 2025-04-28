from django.shortcuts import render
from products.models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def catalog(request):
    return render(request, "catalog.html")
