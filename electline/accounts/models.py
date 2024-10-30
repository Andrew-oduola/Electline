from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser 

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    matric_no = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'matric_no'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.matric_no

    