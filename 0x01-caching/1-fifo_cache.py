#!/usr/bin/env python3
""" 1-basic_cache.py """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    BasicCache is a caching system using FIFO algorithm
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Put a new item in the cache
        """
        if key is None and item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data.keys()))
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')

    def get(self, key):
        """ get a value from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
