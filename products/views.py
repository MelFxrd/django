from django.shortcuts import render
from products.models import Book
from django.views.generic import ListView

class IndexListView (ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"

def catalog(request):
    return render(request, "catalog.html")
