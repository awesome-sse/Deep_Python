"""Testting desc"""
from unittest import TestCase
import unittest
from desc import Data


class TestDataAndDesc(TestCase):
    """Testing Data and Decs"""
    def test_init(self):
        """Testing init"""
        inst = Data(1, 'abc', 2)
        self.assertEqual(inst.num, 1)
        self.assertEqual(inst.name, 'abc')
        self.assertEqual(inst.price, 2)

    def test_desc_change_vals(self):
        """Testing changing values"""
        inst = Data(1, 'abc', 2)
        inst.num = 3
        self.assertEqual(3, inst.num)

        inst.name = 'cba'
        self.assertEqual('cba', inst.name)

        inst.price = 1000
        self.assertEqual(1000, inst.price)

    def test_init_exceptions(self):
        """Testing init with exception"""
        with self.assertRaises(ValueError):
            Data('1', 'abc', 2)

        with self.assertRaises(ValueError):
            Data(1, 2, 3)

        with self.assertRaises(ValueError):
            Data(1, 'abc', 0)

    def test_assign_exceptions(self):
        """Testing changing values with exceptions"""
        inst = Data(1, 'abc', 2)

        with self.assertRaises(ValueError):
            inst.num = 1.2
        self.assertEqual(1, inst.num)

        with self.assertRaises(ValueError):
            inst.name = 1
        self.assertEqual('abc', inst.name)

        with self.assertRaises(ValueError):
            inst.price = -3
        self.assertEqual(2, inst.price)


if __name__ == "__main__":
    unittest.main()
