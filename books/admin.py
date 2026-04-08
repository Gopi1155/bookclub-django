from django.contrib import admin
from .models import Book, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date', 'created_at')
    list_filter = ('genre', 'created_at', 'author')
    search_fields = ('title', 'description', 'author__first_name', 'author__last_name')
    fieldsets = (
        ('Book Info', {'fields': ('title', 'author', 'description', 'genre')}),
        ('Details', {'fields': ('publication_date', 'pages', 'language')}),
        ('Media', {'fields': ('book_file', 'cover_image')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'book')
    search_fields = ('book__title', 'reader__email', 'feedback')
    fieldsets = (
        ('Review Info', {'fields': ('book', 'reader', 'rating', 'feedback')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
