from __future__ import unicode_literals

# Create your models here.
from django.db import models


class MoistureAndTemperatureReport(models.Model):
    reported_at = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    moisture_level = models.FloatField()
