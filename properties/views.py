from django.shortcuts import render
from .models import Property
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties_qs = get_all_properties()
    
    # Convert the QuerySet to a plain list
    properties_list = list(properties_qs)
    return JsonResponse({"data": f"{properties_list}"})