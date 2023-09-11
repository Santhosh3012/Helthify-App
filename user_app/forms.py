from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    pass  # You can customize this form further if needed

from django import forms
from .models import User  # Import your User model if it's defined in models.py

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User  # Use your User model here
        fields = ['username', 'email', 'mobno', 'address', 'gender']  # Add all the fields you want to allow users to update
