from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class MatricNoBackend(ModelBackend):
    def authenticate(self, request, matric_no=None, password=None, *args, **kwargs):
        try:
            user = UserModel.objects.get(matric_no=matric_no)
            if user.check_password(password):
                return user
    
        except UserModel.DoesNotExist:
            return None
        return None
    
    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None