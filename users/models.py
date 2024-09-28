# from django.contrib.auth.models import AbstractUser
# # from django.db import models

# class User(AbstractUser):
#     def __str__(self):
#         return self.first_name
    
    
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.first_name


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db import models

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.first_name
