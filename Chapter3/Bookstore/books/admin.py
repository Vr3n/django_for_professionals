from books.models import Book, Review
from django.contrib import admin

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'price',
    )

    inlines = [ReviewInline, ]

admin.site.register(Book, BookAdmin)