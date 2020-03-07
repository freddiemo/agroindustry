from django.db import models
from django.utils import timezone


class Settlement(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
