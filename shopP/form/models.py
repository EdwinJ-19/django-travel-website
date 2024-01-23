from django.db import models

class form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.DecimalField(max_digits=10,decimal_places=0)
    date_transportation = models.DateField()
    time_transportation = models.TimeField()
    sedan = models.BooleanField(default=False)
    suv = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    van = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    description = models.TextField()
    

    def __str__(self):
        self.first_name

    class Meta:
        db_table = 'form'
