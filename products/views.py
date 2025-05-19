from django.shortcuts import render
from products.models import Book, Author
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse

class IndexListView (ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"

def catalog(request: HttpRequest):
    author = request.GET.get("author")
    year = request.GET.get("year")

    books = Book.objects.all()

    if author:
        books = books.filter(authors=author)

    if year:
        try:
            books = books.filter(date_public__year__gt=int(year))
        except:
            pass

    return render(request, "catalog.html", {"books": books})

def api_get_all_authors(request):
    authors = Author.objects.all()
    dataList = [author.parse_object() for author in authors]
    # safe - чтобы отправить в качестве ответа массив, а не объект, как этого требует JsonResponse
    return JsonResponse(dataList, safe=False)
    
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "book_detail.html", {"book": book})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, "author_detail.html", {"author": author})