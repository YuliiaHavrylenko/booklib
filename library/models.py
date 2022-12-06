from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    description = models.CharField(max_length=2000)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)