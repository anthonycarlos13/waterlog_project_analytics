__author__ = 'anthonymendoza'

from django.db import models


class AggregatedWaterValue(models.Model):
    volume = models.IntegerField(default=0, null=True, blank=True)
    volume_units = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=False)
    total_demand = models.IntegerField(default=0, null=True, blank=True)


class WaterFacilityType(models.Model):
    water_classification_choices = (
        (0, 'OTHER'),
        (1, 'GROUND_WATER'),
        (2, 'RUNOFF_WATER'),
        (3, 'RECYCLED_WATER'),
        (4, 'IMPORTED_WATER'),
        (5, 'DESALINATED_WATER'),
        (6, 'CONSERVED_WATER')
    )
    facility_type = models.CharField(max_length=500, null=True, blank=True)
    volume = models.IntegerField(default=0, null=True, blank=True)
    volume_units = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.facility_type


class WaterFacility(models.Model):
    facility_name = models.CharField(max_length=50, null=True, blank=True)
    facility_type = models.ForeignKey(WaterFacilityType, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    volume = models.IntegerField(default=0, null=True, blank=True)
    volume_units = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=False)
    city = models.CharField(max_length=500, null=True, blank=True)
    county = models.CharField(max_length=500, null=True, blank=True)
    sources = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return "%s : %s" % (self.facility_type, self.facility_name)
