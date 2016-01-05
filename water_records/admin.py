from django.contrib import admin

from .models import AggregatedWaterValue, WaterFacility, WaterFacilityType

admin.site.register(AggregatedWaterValue)
admin.site.register(WaterFacility)
admin.site.register(WaterFacilityType)