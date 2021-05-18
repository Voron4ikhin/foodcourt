from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class UserFC(AbstractUser):
    """ Custom user model
    """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    middle_name = models.CharField(max_length=50, null = True)
    phone = models.CharField(max_length=14, null = True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
