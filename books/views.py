from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from .models import Book, Review
from .forms import BookForm, ReviewForm

@login_required
def dashboard(request):
    """Reader Dashboard - Display all books"""
    books = Book.objects.all()
    search_query = request.GET.get('search', '')
    genre_filter = request.GET.get('genre', '')
    
    if search_query:
        books = books.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    
    if genre_filter:
        books = books.filter(genre__icontains=genre_filter)
    
    # Get genres for filter
    genres = Book.objects.values_list('genre', flat=True).distinct()
    
    # Check if reader has reviewed each book
    reviewed_books = Review.objects.filter(reader=request.user).values_list('book_id', flat=True)
    
    context = {
        'books': books,
        'genres': genres,
        'search_query': search_query,
        'genre_filter': genre_filter,
        'reviewed_books': reviewed_books,
    }
    return render(request, 'books/reader_dashboard.html', context)

@login_required
def book_detail(request, pk):
    """View book details and reviews"""
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    user_review = None
    
    if request.user.is_authenticated and request.user.user_type == 'reader':
        user_review = reviews.filter(reader=request.user).first()
    
    context = {
        'book': book,
        'reviews': reviews,
        'user_review': user_review,
        'average_rating': book.get_average_rating(),
    }
    return render(request, 'books/book_detail.html', context)

@login_required
def add_review(request, pk):
    """Add or edit review for a book"""
    book = get_object_or_404(Book, pk=pk)
    
    # Check if user is a reader
    if request.user.user_type != 'reader':
        messages.error(request, 'Only readers can add reviews.')
        return redirect('books:book_detail', pk=pk)
    
    # Get or create review
    review, created = Review.objects.get_or_create(book=book, reader=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            action = 'created' if created else 'updated'
            messages.success(request, f'Review {action} successfully!')
            return redirect('books:book_detail', pk=pk)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'book': book,
        'form': form,
        'is_edit': not created,
    }
    return render(request, 'books/add_review.html', context)

@login_required
def author_dashboard(request):
    """Author Dashboard - Manage uploaded books"""
    # Check if user is an author
    if request.user.user_type != 'author':
        messages.error(request, 'Only authors can access this page.')
        return redirect('books:dashboard')
    
    books = request.user.books.all()
    
    context = {
        'books': books,
    }
    return render(request, 'books/author_dashboard.html', context)

@login_required
def upload_book(request):
    """Upload a new book"""
    # Check if user is an author
    if request.user.user_type != 'author':
        messages.error(request, 'Only authors can upload books.')
        return redirect('books:dashboard')
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            messages.success(request, 'Book uploaded successfully!')
            return redirect('books:author_dashboard')
    else:
        form = BookForm()
    
    return render(request, 'books/upload_book.html', {'form': form})

@login_required
def edit_book(request, pk):
    """Edit book details"""
    book = get_object_or_404(Book, pk=pk)
    
    # Check if user is the author
    if book.author != request.user:
        messages.error(request, 'You can only edit your own books.')
        return redirect('books:author_dashboard')
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('books:author_dashboard')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, pk):
    """Delete a book"""
    book = get_object_or_404(Book, pk=pk)
    
    # Check if user is the author
    if book.author != request.user:
        messages.error(request, 'You can only delete your own books.')
        return redirect('books:author_dashboard')
    
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('books:author_dashboard')
    
    return render(request, 'books/delete_book.html', {'book': book})

@login_required
def book_reviews(request, pk):
    """View all reviews for a book"""
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    
    context = {
        'book': book,
        'reviews': reviews,
        'average_rating': book.get_average_rating(),
    }
    return render(request, 'books/book_reviews.html', context)

@login_required
def read_book(request, pk):
    """Serve book file for reading/downloading"""
    book = get_object_or_404(Book, pk=pk)
    
    # Check if user is a reader
    if request.user.user_type != 'reader':
        messages.error(request, 'Only readers can access book files.')
        return redirect('books:book_detail', pk=pk)
    
    # Check if book file exists
    if not book.book_file:
        messages.error(request, 'Book file not available.')
        return redirect('books:book_detail', pk=pk)
    
    try:
        # Open and serve the file
        file_path = book.book_file.path
        if not os.path.exists(file_path):
            messages.error(request, 'Book file not found on server.')
            return redirect('books:book_detail', pk=pk)
        
        # Get file extension to determine content type
        file_extension = os.path.splitext(file_path)[1].lower()
        content_types = {
            '.pdf': 'application/pdf',
            '.epub': 'application/epub+zip',
            '.txt': 'text/plain',
            '.doc': 'application/msword',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        }
        
        content_type = content_types.get(file_extension, 'application/octet-stream')
        
        # Read file content
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        # Create response
        response = HttpResponse(file_data, content_type=content_type)
        response['Content-Disposition'] = f'inline; filename="{book.title}{file_extension}"'
        response['Content-Length'] = len(file_data)
        
        return response
        
    except Exception as e:
        messages.error(request, f'Error accessing book file: {str(e)}')
        return redirect('books:book_detail', pk=pk)
