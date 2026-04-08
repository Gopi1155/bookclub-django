from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', limit_choices_to={'user_type': 'author'})
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    book_file = models.FileField(upload_to='books/', help_text='Upload book file (PDF, EPUB, etc.)')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, default='English')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} by {self.author.get_full_name()}"
    
    def get_average_rating(self):
        reviews = self.reviews.filter(rating__isnull=False)
        if reviews.exists():
            return sum([r.rating for r in reviews]) / reviews.count()
        return 0

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    )
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', limit_choices_to={'user_type': 'reader'})
    rating = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('book', 'reader')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Review of {self.book.title} by {self.reader.get_full_name()}"
