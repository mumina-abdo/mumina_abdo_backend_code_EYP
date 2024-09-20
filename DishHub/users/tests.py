from django.test import TestCase

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError  
from .models import User


class UserModelTest(TestCase):
  
   def setUp(self):
       
       self.user = User(
           first_name='John',
           last_name='Doe',
           password='securepassword',
           email='john.doe@example.com'
       )
  
   def test_user_creation(self):
       
       self.user.save()
       self.assertEqual(User.objects.count(), 1)
       self.assertEqual(User.objects.get().email, 'john.doe@example.com')
  
   def test_user_string_representation(self):
    
       self.user.save()
       self.assertEqual(str(self.user), 'John Doe')


   def test_user_password_length(self):
       
       user = User(
           first_name='Jane',
           last_name='Doe',
           password='a' * 17, 
           email='jane.doe@example.com'
       )
       with self.assertRaises(ValidationError):
           user.full_clean()  


   def test_user_unique_email(self):
       
       user1 = User(
           first_name='Alice',
           last_name='Smith',
           password='password123',
           email='alice.smith@example.com'
       )
       user1.save()
       user2 = User(
           first_name='Bob',
           last_name='Brown',
           password='password456',
           email='alice.smith@example.com'  
       )
       try:
           user2.save()
           self.fail("IntegrityError not raised due to duplicate email")
       except IntegrityError:
           pass


   def test_user_missing_required_fields(self):
       
       user = User(
           first_name='',  
           last_name='Doe',
           password='password123',
           email='missing.first.name@example.com'
       )
       with self.assertRaises(ValidationError):
           user.full_clean()  


       user = User(
           first_name='Jane',
           last_name='Doe',
           password='a' * 17,  
           email='missing.password@example.com'
       )
       with self.assertRaises(ValidationError):
           user.full_clean()  

























































































































































































































































































# from django.test import TestCase



# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from django.db.utils import IntegrityError  
# from .models import User

# class UserModelTest(TestCase):
    
#     def setUp(self):

#         self.user = User(
#             first_name='John',
#             last_name='Doe',
#             password='securepassword',
#             email='john.doe@example.com'
#         )
    
#     def test_user_creation(self):

#         self.user.save()
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().email, 'john.doe@example.com')
    
#     def test_user_string_representation(self):

#         self.user.save()
#         self.assertEqual(str(self.user), 'John Doe')

#     def test_user_password_length(self):


#         user = User(
#             first_name='Jane',
#             last_name='Doe',
#             password='a' * 17,  
#             email='jane.doe@example.com'
#         )
#         with self.assertRaises(ValidationError):
#             user.full_clean()  

#     def test_user_unique_email(self):

#         user1 = User(
#             first_name='Alice',
#             last_name='Smith',
#             password='password123',
#             email='alice.smith@example.com'
#         )
#         user1.save()
#         user2 = User(
#             first_name='Bob',
#             last_name='Brown',
#             password='password456',
#             email='alice.smith@example.com'  
#         )
#         try:
#             user2.save()
#             self.fail("IntegrityError not raised due to duplicate email")
#         except IntegrityError:
#             pass

#     def test_user_missing_required_fields(self):
        
#         user = User(
#             first_name='',  
#             last_name='Doe',
#             password='password123',
#             email='missing.first.name@example.com'
#         )
#         with self.assertRaises(ValidationError):
#             user.full_clean()  

#         user = User(
#             first_name='Jane',
#             last_name='Doe',
#             password='a' * 17,  
#             email='missing.password@example.com'
#         )
#         with self.assertRaises(ValidationError):
#             user.full_clean() 
