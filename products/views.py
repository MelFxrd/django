from django.shortcuts import render
from products.models import Book, Author
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse

class IndexListView (ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"

def catalog(request: HttpRequest):
    # Достаю параметр маршрута
    author = request.GET.get("author")
    if (author):
        books = Book.objects.filter(authors=author)
    else:
        books = Book.objects.all()
    return render(request, "catalog.html", {"books": books})

def api_get_all_authors(request):
    authors = Author.objects.all()
    dataList = [author.parse_object() for author in authors]
    # safe - чтобы отправить в качестве ответа массив, а не объект, как этого требует JsonResponse
    return JsonResponse(dataList, safe=False)
    
