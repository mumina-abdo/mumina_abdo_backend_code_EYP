from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
            email='testuser@example.com'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_str_representation(self):
        self.assertEqual(str(self.user), 'Test')

    def test_user_without_username(self):
        with self.assertRaises(ValidationError):
            user = User(username='', password='testpassword')
            user.full_clean()  

    def test_user_without_password(self):
        with self.assertRaises(ValidationError):
            user = User(username='testuser2', password='')
            user.full_clean()  

    def test_user_email_validation(self):
        with self.assertRaises(ValidationError):
            user = User(username='testuser3', password='testpassword', email='not-an-email')
            user.full_clean()  
