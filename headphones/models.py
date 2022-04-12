from django.db import models
from django.contrib.auth.models import User
import datetime

class Headphone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    impedance = models.PositiveSmallIntegerField(default=0)
    frequency = models.TextField(default="0 Hz - 0 KHz")
    sensitivity = models.PositiveSmallIntegerField(default=0)
    def _str_(self):
        return self.title


class Reviews(models.Model):
    headphone = models.ForeignKey(
        Headphone, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    review = models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)
    price_rating = models.IntegerField(default=0)
