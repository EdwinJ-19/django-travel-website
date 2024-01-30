from django.db import models

class form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.DecimalField(max_digits=10,decimal_places=0)
    date_transportation = models.DateField()
    time_transportation = models.TimeField()
    vehicle = models.TextField(max_length=100)
    description = models.TextField()
    passenger = models.IntegerField()
    

    def __str__(self):
        self.first_name

    class Meta:
        db_table = 'form'
