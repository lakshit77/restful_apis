from django.db import models
from RestApp.models import Movie

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    date = models.DateField()