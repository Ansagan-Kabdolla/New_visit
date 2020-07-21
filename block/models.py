from django.db import models
from datetime import datetime

class Zakaz(models.Model):
    organization = models.TextField()
    name = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    first_period = models.DateTimeField()
    second_period = models.DateTimeField()
    iin = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
