from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class ReaderRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False, label="Phone Number")
    roll_no = forms.CharField(max_length=20, required=False, label="Student Roll No")
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'roll_no', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user with this email already exists. Please use a different email.')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone_number')
        roll_no = cleaned_data.get('roll_no')
        if not phone and not roll_no:
            raise forms.ValidationError("Please provide either phone number or roll number")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'reader'
        user.username = user.email
        if commit:
            user.save()
        return user

class AuthorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user with this email already exists. Please use a different email.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'author'
        user.username = user.email
        if commit:
            user.save()
        return user

class ReaderLoginForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    phone_or_roll = forms.CharField(max_length=20, label="Phone Number or Roll No")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class AuthorLoginForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'roll_no', 'bio', 'profile_picture')
