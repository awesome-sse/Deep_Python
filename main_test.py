"""Testting meta class attributes"""
from unittest import TestCase
import unittest
from main import CustomClass


class TestCustomClass(TestCase):
    """Testing CustomClass and its attrs"""

    def test_class_init_attrs(self):
        """Testing Custom init attrs"""

        inst = CustomClass()

        self.assertTrue('custom_x' in dir(inst))
        self.assertFalse('x' in dir(inst))

        self.assertTrue('custom_line' in dir(inst))
        self.assertFalse('line' in dir(inst))

        self.assertTrue('custom_val' in dir(inst))
        self.assertFalse('val' in dir(inst))

    def test_custom_class_init_attrs_values(self):
        """Testing Custom init attrs values"""

        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)

    def test_additional_attrs(self):
        """Testing Custom new attrs"""

        inst = CustomClass()
        inst.attr = "new_attr"
        self.assertTrue('custom_attr' in dir(inst))
        self.assertFalse('attr' in dir(inst))
        self.assertEqual(inst.custom_attr, "new_attr")

    def test_str_custom_class(self):
        """Testing str() CustomClass"""
        inst = CustomClass()

        self.assertTrue('__str__' in dir(inst))
        self.assertFalse('custom___str__' in dir(inst))
        self.assertEqual("Custom_by_metaclass", str(inst))

    def test_new_magic_methon(self):
        """Testing new magic attr CustomClass"""

        def add(self, other):
            return self.custom_x + other.custom_x

        CustomClass.__add__ = add

        inst1 = CustomClass()

        self.assertTrue('__add__' in dir(inst1))
        self.assertFalse('custom___add__' in dir(inst1))

        inst2 = CustomClass()
        inst2.x = 1

        self.assertEqual(inst1 + inst2, 51)


if __name__ == "__main__":
    unittest.main()
