from django.db import models
from djgeojson.fields import PointField


# Create your models here.
class GatheringSpot(models.Model):
    number = models.IntegerField()
    action = models.TextField(max_length=20)
    geom = PointField()
