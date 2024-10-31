from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import re

def is_valid_matric_no(matric_no):
    # Define the regular expression pattern
    pattern = r"^[a-zA-Z]{3}/\d{2}/\d{4}$"
    # Check if the matric number matches the pattern
    return bool(re.match(pattern, matric_no))

class CustomUserManager(BaseUserManager):
    def create_user(self, matric_no, password=None):
        if not matric_no:
            raise ValueError('The Matric number field is required')

        matric_no = matric_no.upper()
        
        # Check matric number format validity
        if not is_valid_matric_no(matric_no):
            raise ValueError('Invalid Matric number format. It should be in the format: ABC/23/1234')

        # Create and save user
        user = self.model(matric_no=matric_no)
        user.set_password(password)
        user.save(using=self._db)
        print('Valid Matric No: %s' % user)
        return user

    def create_superuser(self, matric_no, password=None):
        if not matric_no:
            raise ValueError('The Matric number field is required')

        matric_no = matric_no.upper()
        
        # Check matric number format validity
        if not is_valid_matric_no(matric_no):
            raise ValueError('Invalid Matric number format. It should be in the format: ABC/23/1234')

        # Create and save superuser
        user = self.create_user(matric_no=matric_no, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        print('Valid Matric No: %s' % user)
        return user
