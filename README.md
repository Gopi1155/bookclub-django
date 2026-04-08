# BookClub - Django Web Application

A web application for managing a book club with two user roles: Readers and Authors.

## Features

### For Readers:
- **Registration & Login**: Register with name, phone/roll number, email, and password
- **Dashboard**: Browse all uploaded books with search and genre filter
- **Book Details**: View detailed information about books including cover image
- **Read Books**: Access and read uploaded book files (PDF, EPUB, etc.)
- **Reviews**: Add and edit reviews and ratings for books (1-5 stars)
- **Profile**: Manage personal profile information

### For Authors:
- **Registration & Login**: Register with name, phone number, email, and password
- **Dashboard**: Manage all uploaded books
- **Upload Books**: Upload book files (PDF, EPUB, etc.) with cover images
- **Edit Books**: Modify book details
- **Delete Books**: Remove books from the platform
- **Analytics**: View average ratings and review count for each book

### For Admin:
- **User Management**: View all registered users and their details
- **Book Management**: Manage all books and reviews
- **Analytics**: Monitor user activity and book statistics

## Project Structure

```
BookClub/
├── bookclub/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── books/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── templates/
│   ├── base.html
│   ├── users/
│   │   ├── home.html
│   │   ├── reader_register.html
│   │   ├── reader_login.html
│   │   ├── author_register.html
│   │   ├── author_login.html
│   │   └── profile.html
│   └── books/
│       ├── reader_dashboard.html
│       ├── author_dashboard.html
│       ├── book_detail.html
│       ├── add_review.html
│       ├── upload_book.html
│       ├── edit_book.html
│       ├── delete_book.html
│       └── book_reviews.html
├── manage.py
└── requirements.txt
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps to Run

1. **Clone or Download the Project**
   ```bash
   cd BookClub
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   ```
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Account)**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://localhost:8000/`

## Usage

### First Time Setup

1. Go to `http://localhost:8000/users/home/` - You'll see the home page
2. Choose your role:
   - **Reader**: Click "Register" to create a reader account
   - **Author**: Click "Register" to create an author account

### For Readers
1. Log in with your name, phone/roll number, email, and password
2. Browse books on the dashboard
3. Use search and genre filters to find books
4. Click on a book to view details
5. Add a review and rating for books you've read
6. View and edit your profile

### For Authors
1. Log in with your name, phone number, email, and password
2. Access the author dashboard
3. Click "Upload New Book" to add a book
4. Fill in book details and upload the book file and cover image
5. View analytics for each book (ratings and reviews)
6. Edit or delete your books anytime
7. View and edit your profile

### For Admin
1. Go to `http://localhost:8000/admin/`
2. Log in with your superuser credentials
3. View and manage:
   - **Users**: See all registered readers and authors
   - **Books**: Manage all books in the system
   - **Reviews**: Monitor all reviews and ratings

## Database Models

### User Model
- Extended Django User model
- Fields: `user_type`, `phone_number`, `roll_no`, `profile_picture`, `bio`, `created_at`

### Book Model
- Fields: `title`, `author`, `description`, `genre`, `publication_date`, `book_file`, `cover_image`, `pages`, `language`, `created_at`, `updated_at`

### Review Model
- Fields: `book`, `reader`, `rating`, `feedback`, `created_at`, `updated_at`
- Unique constraint: One review per reader per book

## Key Features

✅ **Two-Role System**: Separate functionality for readers and authors
✅ **User Authentication**: Secure login with email and password
✅ **Book Management**: Upload, edit, and delete books (authors only)
✅ **Review System**: Rate books and write reviews (readers only)
✅ **Search & Filter**: Find books by title, description, or genre
✅ **User Profiles**: Manage personal information and profile pictures
✅ **Admin Panel**: Django admin interface for system management
✅ **Responsive Design**: Bootstrap-based responsive UI

## Technical Stack

- **Backend**: Django 4.2
- **Database**: SQLite3
- **Frontend**: HTML, CSS, Bootstrap 5
- **Image Handling**: Pillow

## Notes

- Book files are uploaded to the `media/books/` directory
- Cover images are stored in `media/book_covers/`
- Profile pictures are stored in `media/profile_pictures/`
- No download feature: Users can only read and review books on the platform

## Security Considerations

- Change `SECRET_KEY` in `settings.py` for production
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Implement HTTPS in production
- Add CSRF protection (already enabled)

## Future Enhancements

- Email verification for registration
- Book recommendations based on reviews
- Discussion forums for book clubs
- Reading progress tracking
- Social features (follow authors, etc.)
- Export reports for admin
- Payment processing for premium features

## Support

For issues or questions, please contact the development team.

---

**Happy Reading! 📚**
