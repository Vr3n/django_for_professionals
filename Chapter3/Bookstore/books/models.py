from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model

# Create your models here.

class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self) -> str:
        return f"{self.title} by {self.author} - ({self.id})"

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews',)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"({self.id}) - {self.review} on {self.book} by {self.author}"