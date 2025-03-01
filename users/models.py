from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ Расширеная модель юзура с автвркой и ролью """
    avatar = models.ImageField(upload_to='images/avatars/', blank=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True, related_name='user')

class Role(models.Model):
    """ Роль для юзера """
    name = models.CharField(max_length=120, unique=True)