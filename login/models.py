from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD: 'email'
    REQUIRED_FIELDS: ['password', 'name']

    def __str__(self):
        return self.email

