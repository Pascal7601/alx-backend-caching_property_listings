from django.core.cache import cache, InvalidCacheBackendError
from .models import Property

def getallproperties():
    queryset = cache.get("allproperties")
    if queryset is None:
        queryset = Property.objects.all()
        cache.set("allproperties", queryset, 3600)
    return queryset
