from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/review/', views.add_review, name='add_review'),
    path('book/<int:pk>/reviews/', views.book_reviews, name='book_reviews'),
    path('book/<int:pk>/read/', views.read_book, name='read_book'),
    path('author/dashboard/', views.author_dashboard, name='author_dashboard'),
    path('upload/', views.upload_book, name='upload_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]
