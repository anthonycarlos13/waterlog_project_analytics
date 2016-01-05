# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AggregatedWaterValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.IntegerField(default=0, null=True, blank=True)),
                ('volume_units', models.CharField(max_length=50, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField()),
                ('total_demand', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterFacility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facility_name', models.CharField(max_length=50, null=True, blank=True)),
                ('latitude', models.CharField(max_length=100, null=True, blank=True)),
                ('longitude', models.CharField(max_length=100, null=True, blank=True)),
                ('volume', models.IntegerField(default=0, null=True, blank=True)),
                ('volume_units', models.CharField(max_length=50, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField()),
                ('city', models.CharField(max_length=500, null=True, blank=True)),
                ('county', models.CharField(max_length=500, null=True, blank=True)),
                ('sources', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterFacilityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facility_type', models.CharField(max_length=500, null=True, blank=True)),
                ('volume', models.IntegerField(default=0, null=True, blank=True)),
                ('volume_units', models.CharField(max_length=50, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='waterfacility',
            name='facility_type',
            field=models.ForeignKey(blank=True, to='water_records.WaterFacilityType', null=True),
        ),
    ]
