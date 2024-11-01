#!/usr/bin/env python3

"""Module defines the `FIFOCache` caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines caching system that
    uses FIFO as its eviction policy

    Inherits:
        -BaseCaching: defines the base caching implementation

    """

    def __init__(self):
        """Initialises the FIFOCache

        Attr:
            cache_keys: list of keys
        """
        super().__init__()
        self.num_of_keys = len(self.cache_data)

    def get(self, key):
        """Gets data linked to key in cache"""
        if key is None:
            return None
        return self.cache_data.get(key)

    def put(self, key, item):
        """Stores data in cache"""
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self._put(key, item)
            return
        if self.num_of_keys >= self.MAX_ITEMS:
            key_to_discard = list(self.cache_data.keys())[0]
            print(f'DISCARD: {key_to_discard}')
            del self.cache_data[key_to_discard]
        else:
            self.num_of_keys += 1
        self._put(key, item)

    def _put(self, key, item):
        """Stores data in cache"""
        self.cache_data[key] = item
