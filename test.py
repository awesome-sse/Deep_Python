"""Testting CustomList class"""
import unittest
from unittest import TestCase
from CustomList import CustomList


class TestCustomList(TestCase):
    """Testing CustomList class"""

    def assert_equal_customlist(self, list1, list2):
        """Assert equals CustomLists"""
        self.assertEqual(len(list1), len(list2))

        for el1, el2 in zip(list1, list2):
            self.assertEqual(el1, el2)

    def test_eq(self):
        """Testing == operator"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        self.assertTrue(list1 == list2)

        list2 = CustomList([2, 2, 2])
        self.assertTrue(list1 == list2)

        list2 = CustomList([1, 2, 2])
        self.assertFalse(list1 == list2)

    def test_ne(self):
        """Testing != operator"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        self.assertFalse(list1 != list2)

        list2 = CustomList([2, 2, 2])
        self.assertFalse(list1 != list2)

        list2 = CustomList([1, 2, 2])
        self.assertTrue(list1 != list2)

    def test_lt(self):
        """Testing < operator"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        self.assertFalse(list1 < list2)

        list2 = CustomList([1, 2, 3, 1])
        self.assertTrue(list1 < list2)

        list2 = CustomList([1, 2, 4])
        self.assertTrue(list1 < list2)

    def test_le(self):
        """Testing <= operator"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        self.assertTrue(list1 <= list2)

        list2 = CustomList([1, 2, 2, 1])
        self.assertTrue(list1 <= list2)

        list2 = CustomList([1, 2, 2])
        self.assertFalse(list1 <= list2)

    def test_gt(self):
        """Testing > operator"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        self.assertFalse(list1 > list2)

        list2 = CustomList([1, 2, 2])
        self.assertTrue(list1 > list2)

        list2 = CustomList([1, 2, 2, 3])
        self.assertFalse(list1 > list2)

    def test_ge(self):
        """Testing >= operator"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 3])
        self.assertTrue(list1 >= list2)

        list2 = CustomList([1, 2, 2])
        self.assertTrue(list1 >= list2)

        list2 = CustomList([1, 2, 2, 3])
        self.assertFalse(list1 >= list2)

    def test_str_(self):
        """Testing str() for CustomList"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, -3])

        self.assertEqual(str(list1),  "[1, 2, 3] 6")
        self.assertEqual(str(list2),  "[1, 2, -3] 0")

    def test_customlist_add_customlist(self):
        """Testing CustomList + CustomList"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, -3])
        list_sum = list1 + list2

        self.assert_equal_customlist(list_sum, CustomList([2, 4, 0]))
        self.assert_equal_customlist(list1, CustomList([1, 2, 3]))
        self.assert_equal_customlist(list2, CustomList([1, 2, -3]))

        list1 = CustomList([1, 2, 3, 2])
        list2 = CustomList([1, 2])
        list_sum = list1 + list2

        self.assert_equal_customlist(list_sum, CustomList([2, 4, 3, 2]))
        self.assert_equal_customlist(list1, CustomList([1, 2, 3, 2]))
        self.assert_equal_customlist(list2, CustomList([1, 2]))

    def test_customlist_sub_customlist(self):
        """Testing CustomList - CustomList"""
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, -3])
        list_sub = list1 - list2

        self.assert_equal_customlist(list_sub, CustomList([0, 0, 6]))
        self.assert_equal_customlist(list1, CustomList([1, 2, 3]))
        self.assert_equal_customlist(list2, CustomList([1, 2, -3]))

        list1 = CustomList([1, 2])
        list2 = CustomList([2, 3, 4, 5])
        list_sub = list1 - list2

        self.assert_equal_customlist(list_sub, CustomList([-1, -1, -4, -5]))
        self.assert_equal_customlist(list1, CustomList([1, 2]))
        self.assert_equal_customlist(list2, CustomList([2, 3, 4, 5]))

    def test_customlist_add_list(self):
        """Testing CustomList + list"""
        list1 = CustomList([1, 2, 3])
        list2 = list([1, 2, -3])
        list_sum = list1 + list2

        self.assert_equal_customlist(list_sum, CustomList([2, 4, 0]))
        self.assert_equal_customlist(list1, CustomList([1, 2, 3]))
        self.assert_equal_customlist(list2, [1, 2, -3])
        self.assertIsInstance(list_sum, CustomList)

        list1 = CustomList([1, 2, 3, 2])
        list2 = list([1, 2])
        list_sum = list1 + list2

        self.assert_equal_customlist(list_sum, CustomList([2, 4, 3, 2]))
        self.assert_equal_customlist(list1, CustomList([1, 2, 3, 2]))
        self.assert_equal_customlist(list2, [1, 2])
        self.assertIsInstance(list_sum, CustomList)

    def test_customlist_sub_list(self):
        """Testing CustomList - list"""
        list1 = CustomList([1, 2, 3])
        list2 = list([1, 2, -3])
        list_sub = list1 - list2

        self.assert_equal_customlist(list_sub, CustomList([0, 0, 6]))
        self.assert_equal_customlist(list1, CustomList([1, 2, 3]))
        self.assert_equal_customlist(list2, [1, 2, -3])
        self.assertIsInstance(list_sub, CustomList)

        list1 = CustomList([1, 2, 3, 4])
        list2 = list([1, 2])
        list_sub = list1 - list2

        self.assert_equal_customlist(list_sub, CustomList([0, 0, 3, 4]))
        self.assert_equal_customlist(list1, CustomList([1, 2, 3, 4]))
        self.assert_equal_customlist(list2, [1, 2])
        self.assertIsInstance(list_sub, CustomList)

    def test_list_add_customlist(self):
        """Testing list + CustomList"""
        list1 = list([1, 2, -3])
        list2 = CustomList([1, 2, 3])
        list_sum = list1 + list2

        self.assert_equal_customlist(list_sum, CustomList([2, 4, 0]))
        self.assert_equal_customlist(list1, [1, 2, -3])
        self.assert_equal_customlist(list2, CustomList([1, 2, 3]))
        self.assertIsInstance(list_sum, CustomList)

        list1 = list([1, 2])
        list2 = CustomList([1, 2, 3, 2])
        list_sum = list1 + list2

        self.assert_equal_customlist(list_sum, CustomList([2, 4, 3, 2]))
        self.assert_equal_customlist(list1, [1, 2])
        self.assert_equal_customlist(list2, CustomList([1, 2, 3, 2]))
        self.assertIsInstance(list_sum, CustomList)

    def test_list_sub_customlist(self):
        """Testing list - CustomList"""
        list1 = list([1, 2, -3])
        list2 = CustomList([1, 2, 3])
        list_sub = list1 - list2

        self.assert_equal_customlist(list_sub, CustomList([0, 0, -6]))
        self.assert_equal_customlist(list1, [1, 2, -3])
        self.assert_equal_customlist(list2, CustomList([1, 2, 3]))
        self.assertIsInstance(list_sub, CustomList)

        list1 = list([1, 2])
        list2 = CustomList([1, 2, 3, 4])
        list_sub = list1 - list2

        self.assert_equal_customlist(list_sub, CustomList([0, 0, -3, -4]))
        self.assert_equal_customlist(list1, [1, 2])
        self.assert_equal_customlist(list2, CustomList([1, 2, 3, 4]))
        self.assertIsInstance(list_sub, CustomList)


if __name__ == "__main__":
    unittest.main()
