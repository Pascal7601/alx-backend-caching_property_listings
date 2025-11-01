from django.core.cache import cache
from .models import Property

def get_all_properties():
    all_properties = cache.get("allproperties")
    if all_properties is None:
        queryset = Property.objects.all()
        cache.set("allproperties", queryset, 3600)
        return queryset
    return all_properties
