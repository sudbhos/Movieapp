from django.db import models

# Create your models here.
class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=100)
    hero=models.CharField(max_length=100)
    herine=models.CharField(max_length=100)
    rating=models.IntegerField()

