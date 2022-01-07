from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    players = ArrayField(models.IntegerField(null=False, blank=False), size=15, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    owner = models.CharField(max_length=255, null=False, blank=False)