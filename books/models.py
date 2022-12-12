from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)  # VARCHAR()
    description = models.TextField()
    isbn = models.CharField(max_length=17)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()