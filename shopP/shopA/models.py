from django.db import models
from django.contrib.auth.models import User

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

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    phone = models.CharField(max_length=10,unique=True)
    class Meta:
        db_table = "USER"

class crud(models.Model):
    head = models.CharField(max_length=50)
    sentence = models.CharField(max_length=200)
    destination = models.CharField(max_length=50,unique=True)
    nearby = models.CharField(max_length=200)
    attraction = models.CharField(max_length=200)
    transportation = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.head

    class Meta:
        db_table = 'travel_card'

class image(models.Model):
    name = models.TextField(max_length=100)
    carousel = models.ImageField(upload_to='carousel_image')

    def __str__(self):
        return self.carousel

    class Meta:
        db_table = 'carousel_img'