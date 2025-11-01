from django.shortcuts import render
from .models import Property
from django.http import JsonResponse
from django.views.decorators.cache import cache_page


@cache_page(60)
def property_list(request):
    properties_qs = Property.objects.values(
        'title', 
        'description', 
        'price', 
        'created_at'
    )
    
    # Convert the QuerySet to a plain list
    properties_list = list(properties_qs)
    return JsonResponse(properties_list, safe=False)