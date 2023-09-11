from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobno = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()

    is_registered = models.BooleanField(default=False) 
    # is_authenticated=models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
    
