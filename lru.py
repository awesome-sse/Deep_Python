"""LRUCache class"""


class LRUCache:
    """LRUCache"""
    def __init__(self, limit=42):
        self.cache = {}
        self.keys = []
        self.limit = limit

    def get(self, key):
        """Function get for lru"""
        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            return self.cache[key]

        return None

    def set(self, key, value):
        """Method set for lru"""
        if key in self.cache:
            self.keys.remove(key)

        else:
            if len(self.keys) >= self.limit:
                last_key = self.keys.pop()
                self.cache.pop(last_key)

        self.keys.insert(0, key)
        self.cache[key] = value
