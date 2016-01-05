from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import WaterFacilityType, WaterFacility, AggregatedWaterValue


def index(request):
    facility_types = WaterFacilityType.objects.all()
    template = loader.get_template('water_records/index.html')
    context = RequestContext(request, {
        'facility_types': facility_types,
    })
    return HttpResponse(template.render(context))


def groundwater(request):
    water_factories_list = WaterFacilityType.objects.filter(water_category_type__category_name__iexact="ground water")
    template = loader.get_template('water_records/groundwater.html')
    context = RequestContext(request, {
        'water_categories_list': water_factories_list,
    })
    return HttpResponse(template.render(context))


def recycledwater(request):
    water_factories_list = WaterFacilityType.objects.filter(water_category_type__category_name__iexact="recycled water")
    template = loader.get_template('water_records/recycledwater.html')
    context = RequestContext(request, {
        'water_categories_list': water_factories_list,
    })
    return HttpResponse(template.render(context))


def runoffwater(request):
    water_factories_list = WaterFacilityType.objects.filter(water_category_type__category_name__iexact="runoff water")
    template = loader.get_template('water_records/runoffwater.html')
    context = RequestContext(request, {
        'water_categories_list': water_factories_list,
    })
    return HttpResponse(template.render(context))


def importedwater(request):
    water_factories_list = WaterFacilityType.objects.filter(water_category_type__category_name__iexact="imported water")
    template = loader.get_template('water_records/importedwater.html')
    context = RequestContext(request, {
        'water_categories_list': water_factories_list,
    })
    return HttpResponse(template.render(context))
