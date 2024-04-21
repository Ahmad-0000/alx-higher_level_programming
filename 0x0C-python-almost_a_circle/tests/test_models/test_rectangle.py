import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_width(self):
        self.assertEqual(Rectangle(12, 13).width, 12)

    def test_width_raises(self):
        self.assertRaises(TypeError, Rectangle, 12.12, 12)
        self.assertRaises(TypeError, Rectangle, "12", 12)
        self.assertRaises(TypeError, Rectangle, True, 12)
        self.assertRaises(TypeError, Rectangle, None, 12)
        self.assertRaises(TypeError, Rectangle, [], 12)
        self.assertRaises(TypeError, Rectangle, {}, 12)
        self.assertRaises(TypeError, Rectangle, (,), 12)
        self.assertRaises(TypeError, Rectangle, {1, 2}, 12)
