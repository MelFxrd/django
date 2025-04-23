from django.db import models

class Author (models.Model):
    name = models.CharField("Полное имя", max_length=80)
    bio = models.TextField("Биография")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book (models.Model):
    title = models.CharField("Название", max_length=120)
    desc = models.TextField("Описание")
    price = models.FloatField("Цена")
    date_public = models.DateField("Дата публикации")
    
    # auto_now_add - добавить дату создания
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    
    # auto_now - добавить дату обновления (т.е. сохранения объекта)
    date_edit = models.DateTimeField("Дата редактирования", auto_now=True)

    authors = models.ManyToManyField(Author, related_name="books", verbose_name="Авторы")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"