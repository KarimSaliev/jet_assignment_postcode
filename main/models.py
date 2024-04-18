from django.db import models

# Create your models here.

class Location(models.Model):
    postcode = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100, null=True)