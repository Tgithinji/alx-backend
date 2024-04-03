#!/usr/bin/env python3
""" 1-basic_cache.py """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system using LIFO algorithm
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Put a new item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item

    def get(self, key):
        """ get a value from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
