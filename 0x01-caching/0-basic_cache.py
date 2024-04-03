#!/usr/bin/env python3
""" 0-basic_cache.py """
BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """
    BasicCache is a caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)