#!/usr/bin/env python3

"""Module defines `BasicCache` caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defines basic caching system

    Inherits
        - BaseCaching: The class defines the base caching implementation
    """

    def put(self, key, item):
        """Add data in cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets data from cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
