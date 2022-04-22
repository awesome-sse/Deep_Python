"""Testting desc"""
from unittest import TestCase
import unittest
from lru import LRUCache


class TestLRUCache(TestCase):
    """Testing LRUCache class"""
    def test_init(self):
        """Testing init LRUCache"""
        lru = LRUCache(10)
        self.assertEqual(lru.cache, {})
        self.assertEqual(lru.keys, [])
        self.assertEqual(lru.limit, 10)

    def test_with_limit_eq_1(self):
        """Testing lru with limit = 1"""
        lru = LRUCache(1)
        lru.set("key1", 1)

        self.assertEqual(lru.get("key1"), 1)
        self.assertEqual(lru.limit, 1)

        lru.set("key2", 2)

        self.assertEqual(lru.get("key1"), None)
        self.assertEqual(lru.get("key2"), 2)

    def test_set_and_get(self):
        """Testing set and get functions"""
        lru = LRUCache(10)
        lru.set(1, 1)
        lru.set(2, 2)

        self.assertTrue(1 in lru.cache)
        self.assertTrue(2 in lru.cache)
        self.assertFalse(3 in lru.cache)

        self.assertTrue(1 in lru.keys)
        self.assertTrue(2 in lru.keys)
        self.assertFalse(3 in lru.keys)

        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), None)

    def test_delete_long_ago_used_key(self):
        """Testing delete element when list overfill"""
        lru = LRUCache(3)
        lru.set(1, 1)
        lru.set(2, 2)
        lru.set(3, 3)

        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)

        lru.get(1)
        lru.set(4, 4)

        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), None)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

    def test_add_elements(self):
        """Testing delete element when list overfill"""
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

    def test_complete_displacement_of_elements(self):
        """Testing complete displacement of elements"""
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")
        cache.set("k4", "val4")

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k4"), "val4")


if __name__ == "__main__":
    unittest.main()
