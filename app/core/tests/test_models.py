from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        '''Test vreting a new user with an email address'''
        email = 'test@gmail.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normailaized(self):
        """ Test the email for a new user is normalized """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email, password='test321')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Testing creating a super user"""
        user = get_user_model().objects.create_superuser(
            'test2020@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    