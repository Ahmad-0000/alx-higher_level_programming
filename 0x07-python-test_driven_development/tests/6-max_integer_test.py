#!/usr/bin/python3
"""
Unittest test cases for a function:
    "max_integer([..])"
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test "max_integer"
    function.
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([-11, -12, -2, -3]), -2)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer(set()), None)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertEqual(max_integer("ahmad"), 'm')

    def test_raises(self):
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.5)
        self.assertRaises(TypeError, max_integer, 5j + 1)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(KeyError, max_integer, {'a': 1, 'b': 2})
        self.assertRaises(TypeError, max_integer, ["ahmad", 1])
        self.assertRaises(TypeError, max_integer, ("ahmad", 1))
        self.assertRaises(TypeError, max_integer, {"ahmad", 1})
