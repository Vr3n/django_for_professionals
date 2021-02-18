from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.title} by {self.author} - ({self.id})"

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])