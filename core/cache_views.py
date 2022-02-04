from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get(license_id):
    return cache.get(license_id)


def update(license_id, license_data):
    cache.set(license_id, license_data, timeout=CACHE_TTL)
    return True


def clear(license_id):
    cache.delete(keys=cache.keys(license_id))
    return True
