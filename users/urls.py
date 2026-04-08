from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('reader/register/', views.reader_register, name='reader_register'),
    path('author/register/', views.author_register, name='author_register'),
    path('reader/login/', views.reader_login, name='reader_login'),
    path('author/login/', views.author_login, name='author_login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
