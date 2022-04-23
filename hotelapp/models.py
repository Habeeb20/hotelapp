from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    no_of_rooms = models.IntegerField()
    address = models.TextField()
    number_of_staffs = models.CharField(max_length=100)
    services = models.TextField()

    def __str__(self):
        return self.name
