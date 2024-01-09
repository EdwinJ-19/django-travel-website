from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(models.Model):
#     email = models.EmailField(max_length=50)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     again_password = models.CharField(max_length=50)

#     def _str_(self):
#         return self.username
    
#     class Meta:
#         db_table='User'

class User(AbstractUser):
    phone = models.CharField(max_length=10,unique=True)
    class Meta:
        db_table = "USER"