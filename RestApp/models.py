from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    date = models.DateField()