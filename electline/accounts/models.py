from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser 

from .managers import CustomUserManager, is_valid_matric_no

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

    def clean(self):
        super().clean()
        if not is_valid_matric_no(self.matric_no):
            raise ValueError("Invalid Matric number format. It should be in the format: ABC/23/1234")

    
    