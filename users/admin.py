from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'phone_number', 'roll_no', 'created_at')
    list_filter = ('user_type', 'created_at')
    search_fields = ('username', 'email', 'phone_number', 'roll_no')
    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'roll_no')}),
        ('Account', {'fields': ('username', 'user_type', 'password')}),
        ('Profile', {'fields': ('profile_picture', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
