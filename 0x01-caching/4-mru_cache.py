#!/usr/bin/env python3

"""Module defines the `MRUCache` caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Defines caching system that
    uses MRU (Most Recently Used) as its eviction policy

    Inherits:
        -BaseCaching: defines the base caching implementation

    """

    def __init__(self):
        """Initialises the MRUCache

        Attr:
            cache_keys: list of keys
        """
        super().__init__()
        self.num_of_keys = len(self.cache_data)
        self.accessed_keys = []

    def get(self, key):
        """Gets data linked to key in cache"""
        if key is None:
            return None
        data = self.cache_data.get(key)
        if data is None:
            return None
        self.update_accessed_keys(key)
        return data

    def put(self, key, item):
        """Stores data in cache"""
        if key is None or item is None:
            return

        key_exists = self.is_key_exists(key)
        if self.is_cache_full() and not key_exists:
            key_to_discard = self.get_key_to_discard()
            print(f'DISCARD: {key_to_discard}')
            del self.cache_data[key_to_discard]
        self.num_of_keys += 1 if not key_exists else 0
        self._put(key, item)

    def is_key_exists(self, key) -> bool:
        """Checks if key exists in cache"""
        return key in self.cache_data.keys()

    def is_cache_full(self) -> bool:
        """Checks whether cache is full"""
        return self.num_of_keys >= self.MAX_ITEMS

    def get_key_to_discard(self):
        """Gets key to remove"""
        return self.accessed_keys.pop(-1)

    def update_accessed_keys(self, key):
        """Updates the accessed keys"""
        if key in self.accessed_keys:
            self.accessed_keys.remove(key)
        self.accessed_keys.append(key)

    def _put(self, key, item):
        """Stores data in cache"""
        self.update_accessed_keys(key)
        self.cache_data[key] = item
