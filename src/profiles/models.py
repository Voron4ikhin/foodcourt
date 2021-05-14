from django.contrib.auth.models import AbstractUser
from django.db import models


class OrdUser(AbstractUser):
    """Custom user model"""
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)

