# from django.contrib.auth.models import User
# class Auth0Backend:
#     def authenticate(self, request, user_info=None):
#         if user_info:
#             user, created = User.objects.get_or_create(username=user_info['email'])
#             if created:
#                 user.email = user_info['email']
#                 user.save()
#             return user
#         return None

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Auth0Backend:
    def authenticate(self, request, user_info=None):
        if user_info:
            email = user_info['email']  # Use email directly
            try:
                user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                user = User(email=email)
                user.set_unusable_password()  # If you don’t want to set a password
                user.save()  # Save the new user instance
            
            return user
        return None
