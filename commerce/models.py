from django.db import models
from django.utils import timezone


class Commerce(models.Model):
    name = models.CharField(max_length=30)
    nit = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
