from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser):
    matric_no = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'matric_no'

    