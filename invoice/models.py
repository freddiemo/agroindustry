from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    date = models.DateTimeField()
    amount = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
