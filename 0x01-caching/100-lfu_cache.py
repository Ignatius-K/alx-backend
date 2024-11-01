#!/usr/bin/env python3

"""Module defines the `LFUCache` caching system"""

from base_caching import BaseCaching
from collections import Counter


class LFUCache(BaseCaching):
    """Defines caching system that
    uses LFU (Least Frequently Used) as its eviction policy

    Inherits:
        -BaseCaching: defines the base caching implementation

    """

    def __init__(self):
        """Initialises the LFUCache

        Attr:
            cache_keys: list of keys
        """
        super().__init__()
        self.num_of_keys = len(self.cache_data)
        self.access_counter = Counter()

    def get(self, key):
        """Gets data linked to key in cache"""
        if key is None:
            return None
        data = self.cache_data.get(key)
        if data is None:
            return None
        self.update_counter(key)
        return data

    def put(self, key, item):
        """Stores data in cache"""
        if key is None or item is None:
            return

        key_exists = self.is_key_exists(key)
        if self.is_cache_full() and not key_exists:
            key_to_discard = self.get_key_to_discard()
            print(f'DISCARD: {key_to_discard}')
            del self.access_counter[key_to_discard]
            del self.cache_data[key_to_discard]
        self.num_of_keys += 1 if not key_exists else 0
        self._put(key, item)

    def is_key_exists(self, key) -> bool:
        """Checks if key exists in cache"""
        return key in self.cache_data.keys()

    def is_cache_full(self) -> bool:
        """Checks whether cache is full"""
        return self.num_of_keys >= self.MAX_ITEMS

    def update_counter(self, key):
        """Updates the counter"""
        self.access_counter.update(key)

    def get_key_to_discard(self):
        """Gets key to remove"""
        return min(self.access_counter, key=self.access_counter.get)

    def _put(self, key, item):
        """Stores data in cache"""
        self.update_counter(key)
        self.cache_data[key] = item
