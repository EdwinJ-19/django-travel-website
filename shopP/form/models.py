from django.db import models

class form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.DecimalField()
    date_transportation = models.DateField()
    time_transportation = models.TimeField()
    sedan = models.BooleanField(default=False)
    suv = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    van = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    description = models.TextField()
    
