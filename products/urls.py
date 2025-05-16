from django.urls import path
from products.views import *

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("catalog/", catalog, name="catalog"),
    path("all-authors/", api_get_all_authors, name="api_all_authors"),
    path("book/<int:pk>/", book_detail, name="book_detail"),
    path("author/<int:pk>/", author_detail, name="author_detail"),
]