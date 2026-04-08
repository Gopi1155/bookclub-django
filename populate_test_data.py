# Script to populate test data
# WARNING: This script adds demo data for testing purposes only.
# To remove demo data, run: python remove_demo_data.py
#
# This script creates:
# - 2 demo readers (reader1@test.com, reader2@test.com)
# - 2 demo authors (author1@test.com, author2@test.com)
# - 3 demo books with reviews
#
# For production use, real users should register through the application.

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookclub.settings')
django.setup()

from django.contrib.auth import get_user_model
from books.models import Book, Review

User = get_user_model()

print("Creating test data...")
print("⚠️  WARNING: This adds demo data. Use remove_demo_data.py to clean up.")

# Create test readers
print("\nCreating test readers...")
reader1, created = User.objects.get_or_create(
    email='reader1@test.com',
    defaults={
        'username': 'reader1@test.com',
        'first_name': 'Alice',
        'last_name': 'Johnson',
        'user_type': 'reader',
        'phone_number': '9876543210'
    }
)
if created:
    reader1.set_password('reader123')
    reader1.save()
    print(f"✓ Created reader: {reader1.get_full_name()}")
else:
    print(f"✓ Reader already exists: {reader1.get_full_name()}")

reader2, created = User.objects.get_or_create(
    email='reader2@test.com',
    defaults={
        'username': 'reader2@test.com',
        'first_name': 'Bob',
        'last_name': 'Smith',
        'user_type': 'reader',
        'roll_no': 'CS001'
    }
)
if created:
    reader2.set_password('reader123')
    reader2.save()
    print(f"✓ Created reader: {reader2.get_full_name()}")
else:
    print(f"✓ Reader already exists: {reader2.get_full_name()}")

# Create test authors
print("\nCreating test authors...")
author1, created = User.objects.get_or_create(
    email='author1@test.com',
    defaults={
        'username': 'author1@test.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'user_type': 'author',
        'phone_number': '9876543211'
    }
)
if created:
    author1.set_password('author123')
    author1.save()
    print(f"✓ Created author: {author1.get_full_name()}")
else:
    print(f"✓ Author already exists: {author1.get_full_name()}")

author2, created = User.objects.get_or_create(
    email='author2@test.com',
    defaults={
        'username': 'author2@test.com',
        'first_name': 'Jane',
        'last_name': 'Williams',
        'user_type': 'author',
        'phone_number': '9876543212'
    }
)
if created:
    author2.set_password('author123')
    author2.save()
    print(f"✓ Created author: {author2.get_full_name()}")
else:
    print(f"✓ Author already exists: {author2.get_full_name()}")

# Create test books
print("\nCreating test books...")
book1, created = Book.objects.get_or_create(
    title='The Great Gatsby',
    author=author1,
    defaults={
        'description': 'A classic novel about the American Dream set in the Jazz Age.',
        'genre': 'Fiction',
        'pages': 180,
        'language': 'English'
    }
)
if created:
    print(f"✓ Created book: {book1.title}")
else:
    print(f"✓ Book already exists: {book1.title}")

book2, created = Book.objects.get_or_create(
    title='To Kill a Mockingbird',
    author=author2,
    defaults={
        'description': 'A compelling tale of racial injustice and moral awakening in the American South.',
        'genre': 'Fiction',
        'pages': 281,
        'language': 'English'
    }
)
if created:
    print(f"✓ Created book: {book2.title}")
else:
    print(f"✓ Book already exists: {book2.title}")

book3, created = Book.objects.get_or_create(
    title='1984',
    author=author1,
    defaults={
        'description': 'A dystopian novel depicting a totalitarian state.',
        'genre': 'Science Fiction',
        'pages': 328,
        'language': 'English'
    }
)
if created:
    print(f"✓ Created book: {book3.title}")
else:
    print(f"✓ Book already exists: {book3.title}")

# Create test reviews
print("\nCreating test reviews...")
try:
    review1, created = Review.objects.get_or_create(
        book=book1,
        reader=reader1,
        defaults={
            'rating': 5,
            'feedback': 'An absolutely masterpiece! Fitzgerald\'s prose is captivating and the story is timeless.'
        }
    )
    if created:
        print(f"✓ Created review for {book1.title} by {reader1.get_full_name()}")
except:
    print(f"⚠ Review already exists for {book1.title} by {reader1.get_full_name()}")

try:
    review2, created = Review.objects.get_or_create(
        book=book1,
        reader=reader2,
        defaults={
            'rating': 4,
            'feedback': 'Great book with beautiful writing. A must-read for all literature enthusiasts.'
        }
    )
    if created:
        print(f"✓ Created review for {book1.title} by {reader2.get_full_name()}")
except:
    print(f"⚠ Review already exists for {book1.title} by {reader2.get_full_name()}")

try:
    review3, created = Review.objects.get_or_create(
        book=book2,
        reader=reader1,
        defaults={
            'rating': 5,
            'feedback': 'One of the greatest novels ever written. Deeply moving and thought-provoking.'
        }
    )
    if created:
        print(f"✓ Created review for {book2.title} by {reader1.get_full_name()}")
except:
    print(f"⚠ Review already exists for {book2.title} by {reader1.get_full_name()}")

try:
    review4, created = Review.objects.get_or_create(
        book=book3,
        reader=reader2,
        defaults={
            'rating': 5,
            'feedback': 'Chilling and prophetic. Orwell\'s vision is frighteningly relevant even today.'
        }
    )
    if created:
        print(f"✓ Created review for {book3.title} by {reader2.get_full_name()}")
except:
    print(f"⚠ Review already exists for {book3.title} by {reader2.get_full_name()}")

print("\n✅ Test data setup complete!")
print("\nTest Credentials:")
print("=" * 50)
print("ADMIN")
print("  Username: admin")
print("  Password: admin123")
print("\nREADERS")
print("  Email: reader1@test.com | Password: reader123")
print("  Email: reader2@test.com | Password: reader123")
print("\nAUTHORS")
print("  Email: author1@test.com | Password: author123")
print("  Email: author2@test.com | Password: author123")
print("=" * 50)
