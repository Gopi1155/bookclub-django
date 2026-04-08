# BookClub Django App - Quick Start Guide

## ✅ Project Setup Complete!

Your Django BookClub application is now fully configured and running!

## 🚀 How to Access the Application

The application is currently running at: **http://localhost:8000/**

### Home Page
Navigate to: `http://localhost:8000/users/home/`

## 📋 Quick Links

### User Registration & Login
- **Reader Registration**: `http://localhost:8000/users/reader/register/`
- **Reader Login**: `http://localhost:8000/users/reader/login/`
- **Author Registration**: `http://localhost:8000/users/author/register/`
- **Author Login**: `http://localhost:8000/users/author/login/`

### Dashboards (After Login)
- **Reader Dashboard**: `http://localhost:8000/books/dashboard/`
- **Author Dashboard**: `http://localhost:8000/books/author/dashboard/`

### Admin Panel
- **Admin Interface**: `http://localhost:8000/admin/`
- **Username**: `admin`
- **Password**: `admin123`

## 🧪 Test Credentials

### Admin Account
```
Username: admin
Email: admin@bookclub.com
Password: admin123
```

## 📝 Create Your First Test Accounts

### To Create a Reader Account:
1. Go to `http://localhost:8000/users/home/`
2. Click "Reader Registration"
3. Fill in the form:
   - First Name: John
   - Last Name: Doe
   - Email: john@example.com
   - Phone Number: 9876543210 (or Roll No: 12345)
   - Password: TestPass123!
4. Click Register

### To Create an Author Account:
1. Go to `http://localhost:8000/users/home/`
2. Click "Author Registration"
3. Fill in the form:
   - First Name: Jane
   - Last Name: Smith
   - Email: jane@example.com
   - Phone Number: 9876543211
   - Password: TestPass123!
4. Click Register

## 🎯 Key Features to Test

### For Readers:
- ✅ Register and login with email and phone/roll number
- ✅ Browse all books on the dashboard
- ✅ Search books by title or description
- ✅ Filter books by genre
- ✅ View book details including cover image
- ✅ Add and edit reviews (1-5 star ratings)
- ✅ View all reviews for a book
- ✅ Update profile information

### For Authors:
- ✅ Register and login with email and phone number
- ✅ Upload books with details (title, description, genre, etc.)
- ✅ Upload book file (PDF, EPUB, etc.)
- ✅ Upload cover image
- ✅ View uploaded books on author dashboard
- ✅ Edit book information
- ✅ Delete books
- ✅ View average rating and review count for each book
- ✅ Update profile information

### For Admin:
- ✅ View all registered users (readers and authors)
- ✅ View all uploaded books
- ✅ View all reviews and ratings
- ✅ Edit or delete users, books, and reviews
- ✅ Access detailed user information

## 📁 Project Structure

```
BookClub/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database (auto-created)
├── README.md                # Full documentation
├── bookclub/                # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                   # User app (registration, login, profiles)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── books/                   # Books app (CRUD, reviews)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── templates/               # HTML templates
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
├── media/                   # Uploaded files
│   ├── books/              # Book files
│   ├── book_covers/        # Book cover images
│   └── profile_pictures/   # User profile pictures
└── static/                  # Static files (CSS, JS, images)
```

## 🛠️ Useful Commands

### Start the Development Server
```bash
python manage.py runserver
```

### Access Django Shell
```bash
python manage.py shell
```

### Create a Superuser
```bash
python manage.py createsuperuser
```

### Make Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## 📊 Database Models

### User Model
- ID, Username, Email, First Name, Last Name
- User Type (Reader or Author)
- Phone Number, Roll Number (for students)
- Profile Picture, Bio
- Created Date

### Book Model
- ID, Title, Author, Description
- Genre, Language, Publication Date
- Book File (PDF, EPUB, etc.)
- Cover Image, Number of Pages
- Created/Updated Dates

### Review Model
- ID, Book, Reader, Rating (1-5)
- Feedback Text
- Created/Updated Dates
- Unique constraint: One review per reader per book

## 🔐 Security Notes

For production use:
1. Change the `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False` in `settings.py`
3. Update `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Set up HTTPS
6. Create environment variables for sensitive data

## 🐛 Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```bash
python manage.py runserver 8001
```

### Database Issues
To reset the database:
```bash
# Delete the database file
rm db.sqlite3

# Recreate database
python manage.py migrate
python manage.py createsuperuser
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## 📚 Additional Features to Add

Potential enhancements:
- Email verification for registration
- Password reset functionality
- Book recommendations based on reviews
- Discussion forums
- Reading progress tracking
- Social features (follow authors, wishlist)
- Payment processing
- Advanced search and filters

## 📞 Support

For issues or questions, refer to the README.md file for comprehensive documentation.

---

## ✨ You're All Set!

Your BookClub application is ready to use. Start by:
1. Visiting `http://localhost:8000/users/home/`
2. Creating test reader and author accounts
3. Uploading some test books
4. Adding reviews
5. Exploring the admin panel

**Happy coding! 📚**
