
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager\



class CustomUserManager(BaseUserManager):
    def create_user(self, matric_no, password=None):
        if not matric_no:
            raise ValueError('The Matric number field is required')
        
        user = self.model(matric_no=matric_no)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matric_no, password=None):
        user = self.create_user(matric_no=matric_no, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
