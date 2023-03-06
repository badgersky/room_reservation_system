from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    seat_number = models.SmallIntegerField()
    projector = models.BooleanField()
