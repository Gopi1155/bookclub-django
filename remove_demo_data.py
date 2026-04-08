# Script to remove demo/test data
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookclub.settings')
django.setup()

from django.contrib.auth import get_user_model
from books.models import Book, Review

User = get_user_model()

print("Removing demo data...")

# Remove test reviews first (due to foreign key constraints)
print("\nRemoving test reviews...")
reviews_deleted = 0
try:
    # Remove reviews for demo books
    demo_books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984']
    for book_title in demo_books:
        try:
            book = Book.objects.get(title=book_title)
            deleted_count = Review.objects.filter(book=book).delete()[0]
            reviews_deleted += deleted_count
            print(f"✓ Removed {deleted_count} reviews for '{book_title}'")
        except Book.DoesNotExist:
            print(f"⚠ Book '{book_title}' not found")
except Exception as e:
    print(f"⚠ Error removing reviews: {e}")

# Remove test books
print("\nRemoving test books...")
books_deleted = 0
demo_books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984']
for book_title in demo_books:
    try:
        book = Book.objects.get(title=book_title)
        book.delete()
        books_deleted += 1
        print(f"✓ Removed book: '{book_title}'")
    except Book.DoesNotExist:
        print(f"⚠ Book '{book_title}' not found")

# Remove test users (optional - uncomment if you want to remove demo users too)
print("\nRemoving test users...")
users_deleted = 0
demo_users = ['reader1@test.com', 'reader2@test.com', 'author1@test.com', 'author2@test.com']
for email in demo_users:
    try:
        user = User.objects.get(email=email)
        user.delete()
        users_deleted += 1
        print(f"✓ Removed user: {email}")
    except User.DoesNotExist:
        print(f"⚠ User '{email}' not found")

print("\n✅ Demo data removal complete!")
print(f"📊 Summary:")
print(f"   Books removed: {books_deleted}")
print(f"   Reviews removed: {reviews_deleted}")
print(f"   Users removed: {users_deleted}")
print("\nNote: Admin user (admin/admin123) was preserved.")
print("Real authors can now upload their own books through the application.")