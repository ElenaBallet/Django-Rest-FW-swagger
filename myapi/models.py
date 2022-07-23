from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        ordering = ('name',)


class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ad'
        verbose_name_plural = 'ads'
        ordering = ('title',)

    def authors_names(self) -> list:
        return [a.name for a in self.authors.all()]
