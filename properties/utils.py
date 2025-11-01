from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    all_properties = cache.get("allproperties")
    if all_properties is None:
        queryset = Property.objects.all()
        cache.set("allproperties", queryset, 3600)
        return queryset
    return all_properties

def get_redis_cache_metrics():
    """
    Connects to the default Redis cache and retrieves keyspace
    hit/miss metrics and calculates the hit ratio.
    
    Returns:
        A dictionary with hits, misses, total_requests, and hit_ratio.
    """
    try:
        client = get_redis_connection("default")
        
        # 2. Get the full server INFO dictionary
        info = client.info()
      
        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total_requests = hits + misses

        hit_ratio = 0.0  # Default to 0.0
        if total_requests > 0:
            hit_ratio = hits / total_requests
        else:
            total_requests = 0

        logger.info(
            f"[Cache Metrics] Hits: {hits}, Misses: {misses}, "
            f"total_requests: {total_requests}, Hit Ratio: {hit_ratio:.2%}"
        )
        
        return {
            "hits": hits,
            "misses": misses,
            "total_requests": total_requests,
            "hit_ratio": hit_ratio,
            "hit_ratio_percent": f"{hit_ratio:.2%}"
        }

    except Exception as e:
        logger.error(f"Could not retrieve Redis cache metrics: {e}")
        return {
            "hits": 0,
            "misses": 0,
            "total_requests": 0,
            "hit_ratio": 0.0,
            "hit_ratio_percent": "0.00%",
            "error": str(e)
        }