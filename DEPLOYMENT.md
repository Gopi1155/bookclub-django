# BookClub Production Deployment Guide

## 📦 Pre-Deployment Checklist

### Security
- [ ] Change SECRET_KEY in settings.py (use a strong random value)
- [ ] Set DEBUG = False
- [ ] Set ALLOWED_HOSTS to your domain
- [ ] Use HTTPS (SSL/TLS certificates)
- [ ] Set secure session and CSRF cookies
- [ ] Configure CORS if needed
- [ ] Set up environment variables for sensitive data

### Database
- [ ] Migrate from SQLite to PostgreSQL or MySQL
- [ ] Set up database backups
- [ ] Configure connections/pooling

### Static & Media Files
- [ ] Run: `python manage.py collectstatic`
- [ ] Set up CDN or static file server
- [ ] Configure media file storage

### Performance
- [ ] Set up caching (Redis)
- [ ] Enable compression
- [ ] Optimize images
- [ ] Configure cache headers

### Monitoring
- [ ] Set up error logging (Sentry)
- [ ] Enable access logging
- [ ] Monitor database performance
- [ ] Set up alerts

---

## 🔧 Environment Configuration

### Create .env file
```env
# Django Settings
DEBUG=False
SECRET_KEY=your-secret-key-here-generate-a-random-one
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=bookclub_db
DB_USER=bookclub_user
DB_PASSWORD=secure_password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# AWS S3 (for media storage)
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
```

### Update settings.py for production
```python
import os
from pathlib import Path

# Load environment variables
import environ
env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': env('DB_NAME', 'db.sqlite3'),
        'USER': env('DB_USER', ''),
        'PASSWORD': env('DB_PASSWORD', ''),
        'HOST': env('DB_HOST', 'localhost'),
        'PORT': env('DB_PORT', '5432'),
    }
}

# Security Settings
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', False)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', False)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', 0)

# Email Configuration
EMAIL_BACKEND = env('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', '')
EMAIL_PORT = env.int('EMAIL_PORT', 587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', True)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')
```

---

## 🗄️ Database Migration (SQLite to PostgreSQL)

### 1. Install PostgreSQL
```bash
# Windows: Download from https://www.postgresql.org/download/windows/
# macOS: brew install postgresql
# Linux: sudo apt-get install postgresql
```

### 2. Create Database and User
```sql
CREATE DATABASE bookclub_db;
CREATE USER bookclub_user WITH PASSWORD 'secure_password';
ALTER ROLE bookclub_user SET client_encoding TO 'utf8';
ALTER ROLE bookclub_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE bookclub_user SET default_transaction_deferrable TO on;
ALTER ROLE bookclub_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bookclub_db TO bookclub_user;
```

### 3. Backup SQLite Data
```bash
python manage.py dumpdata > backup.json
```

### 4. Update Database Settings
```bash
pip install psycopg2-binary
# Update DATABASE in settings.py to use PostgreSQL
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Restore Data
```bash
python manage.py loaddata backup.json
```

---

## 🚀 Deployment Options

### Option 1: Heroku
```bash
# Install Heroku CLI
# Login
heroku login

# Create app
heroku create bookclub-app

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

### Option 2: AWS EC2
```bash
# 1. Launch EC2 instance (Ubuntu)
# 2. Connect via SSH
# 3. Install dependencies
sudo apt update
sudo apt install python3-pip python3-venv postgresql nginx

# 4. Clone repository
git clone your-repo-url
cd BookClub

# 5. Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 6. Configure Gunicorn
pip install gunicorn

# 7. Run migrations
python manage.py migrate

# 8. Collect static files
python manage.py collectstatic --noinput

# 9. Configure Nginx
# 10. Configure Gunicorn service
# 11. Start services
```

### Option 3: DigitalOcean App Platform
```bash
# 1. Connect GitHub repository
# 2. Set environment variables in App Platform dashboard
# 3. Configure PostgreSQL database
# 4. Deploy
```

### Option 4: PythonAnywhere
```bash
# 1. Upload files via web interface
# 2. Create virtual environment
# 3. Configure Django web app
# 4. Set environment variables
# 5. Reload app
```

---

## 🔐 SSL/HTTPS Setup

### Using Let's Encrypt (Free)
```bash
# Install Certbot
sudo apt-get install certbot python3-certbot-nginx

# Generate certificate
sudo certbot certonly --nginx -d yourdomain.com

# Auto-renewal
sudo certbot renew --dry-run
```

### Update Django Settings
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

---

## 📊 Performance Optimization

### Enable Caching (Redis)
```bash
pip install django-redis
```

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### CDN Configuration (CloudFlare)
```python
# settings.py
STATIC_URL = 'https://cdn.yourdomain.com/static/'
MEDIA_URL = 'https://cdn.yourdomain.com/media/'
```

### Database Optimization
```python
# Use select_related and prefetch_related
books = Book.objects.select_related('author').prefetch_related('reviews')
```

---

## 📈 Monitoring & Logging

### Sentry Error Tracking
```bash
pip install sentry-sdk
```

```python
# settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=False
)
```

### Logging Configuration
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

---

## 🔄 Backup & Recovery

### Automated Database Backups
```bash
# Weekly backup script
0 2 * * 0 /home/user/backup.sh

# backup.sh
#!/bin/bash
pg_dump -U bookclub_user bookclub_db | gzip > /backups/bookclub_$(date +%Y%m%d).sql.gz
```

### Media File Backups
```bash
# Use AWS S3, Google Cloud Storage, or similar
# Or rsync to external server
rsync -avz /var/www/bookclub/media/ backup@backupserver:/backups/bookclub/media/
```

---

## 📋 Deployment Checklist

Before going live:
- [ ] Update SECRET_KEY
- [ ] Set DEBUG = False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up HTTPS/SSL
- [ ] Configure database (PostgreSQL)
- [ ] Set up email (SendGrid, AWS SES, etc.)
- [ ] Configure static/media files
- [ ] Set up error tracking (Sentry)
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Test all features in production
- [ ] Set up automated backups
- [ ] Configure CDN
- [ ] Set up health check endpoint
- [ ] Test email functionality
- [ ] Test file uploads
- [ ] Test admin panel
- [ ] Load test the application
- [ ] Security audit
- [ ] Get SSL certificate
- [ ] Set up firewall rules
- [ ] Configure rate limiting

---

## 🆘 Troubleshooting Deployment

### Application Won't Start
```bash
# Check logs
tail -f /var/log/django/error.log

# Check migrations
python manage.py showmigrations

# Run migrations
python manage.py migrate
```

### 500 Internal Server Error
- Check Django error logs
- Enable DEBUG temporarily to see error
- Check database connection
- Check file permissions

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
# Check web server configuration
```

### Database Connection Issues
```bash
# Test connection
python manage.py dbshell

# Check credentials
# Check firewall/security groups
```

---

## 📞 Support & Resources

- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Heroku Django: https://devcenter.heroku.com/articles/deploying-python
- DigitalOcean App Platform: https://www.digitalocean.com/products/app-platform/
- AWS EC2: https://aws.amazon.com/ec2/
- PostgreSQL: https://www.postgresql.org/docs/

---

**Good luck with your deployment! 🚀**
