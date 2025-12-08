from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('applicant', 'Applicant'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),

    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='applicant')
    # username = models.CharField(max_length=150, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
     


    def __str__(self):
        return self.username
