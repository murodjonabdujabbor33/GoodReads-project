from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)  # VARCHAR()
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    