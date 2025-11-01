from django.shortcuts import render
from .models import Property
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties, get_redis_cache_metrics

@cache_page(60 * 15)
def property_list(request):
    properties_qs = get_all_properties()
    
    # Convert the QuerySet to a plain list
    properties_list = list(properties_qs)
    return JsonResponse({"data": f"{properties_list}"})

def property_cache_metrics(request):
    """
    A view that returns the current cache metrics as JSON.
    """
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)