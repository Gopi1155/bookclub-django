from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'genre', 'publication_date', 'book_file', 'cover_image', 'pages', 'language')
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'feedback')
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4}),
        }
