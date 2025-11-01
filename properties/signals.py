from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Property
from django.core.cache import cache


@receiver([post_delete, post_save], sender=Property)
def update_cache(sender, instance, **kwargs):
    cache.delete("allproperties")

