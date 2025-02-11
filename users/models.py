from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/avatars/', blank=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True, related_name='user')

class Role(models.Model):
    name = models.CharField(max_length=120, unique=True)