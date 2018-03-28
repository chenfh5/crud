from django.db import models
from django.utils import timezone


# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=50, null=False)
    isbn = models.CharField(max_length=20, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author + ' <<' + self.title + '>>'
