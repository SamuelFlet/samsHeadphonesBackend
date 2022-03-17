from django.db import models
from django.contrib.auth import get_user_model


class Headphone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.title


class Reviews(models.Model):
    headphone = models.ForeignKey(
        Headphone, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.TextField()
    price_rating = models.IntegerField(null=True)
