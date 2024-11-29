from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"
