import datetime
from django.db import models

class WomenCycle(models.Model):
    last_period_date = models.DateField(blank=True, null=True)
    cycle_average = models.IntegerField(default=25)
    Period_average = models.IntegerField(default=5)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.last_period_date

class GeneratedCycle(models.Model):
    event =  models.CharField(max_length=255, null=True)
    date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.period_start_date


