from django.test import TestCase
from django.core.exceptions import ValidationError
from django.test import Client
from django.urls import reverse
from .models import CustomUser

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(matric_no='CSC/23/3986', password='password123')
        self.password = 'password123'

    def test_create_user(self):
        self.assertEqual(self.user.matric_no, 'CSC/23/3986')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(matric_no='CSC/23/1234', password='password123')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_create_user_with_invalid_matric_no(self):
        with self.assertRaises(ValidationError) as context:
            CustomUser.objects.create_user(matric_no='3986', password='password123')
        self.assertEqual(str(context.exception), "['Invalid Matric number format. It should be in the format: ABC/23/1234']")

    
class ClientTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(matric_no='CSC/23/3986', password='password123')
        self.client = Client()  # Initialize the Client here

    def test_client_login(self):
        # Using the client to log in
        login_success = self.client.login(matric_no=self.user.matric_no, password='password123')
        self.assertTrue(login_success)  # Check if login was successful

        # Testing login via POST request on the login URL
        response = self.client.post(reverse('accounts:login'), {'matric_no': self.user.matric_no, 'password': 'password123'})
        self.assertEqual(response.status_code, 302) 

