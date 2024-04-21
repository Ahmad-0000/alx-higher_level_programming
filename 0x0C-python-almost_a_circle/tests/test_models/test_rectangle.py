import sys
import unittest


sys.path.append('..')
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_min_args(self):
        r_obj = Rectangle(5, 10)
        self.assertEqual(r_obj.width, 5)
        self.assertEqual(r_obj.height, 10)
        self.assertEqual(r_obj.x, 0)
        self.assertEqual(r_obj.y, 0)
    
    def test_max_args(self):
        r_obj = Rectangle(5, 10, 12, 12, 12)
        self.assertEqual(r_obj.width, 5)
        self.assertEqual(r_obj.height, 10)
        self.assertEqual(r_obj.x, 12)
        self.assertEqual(r_obj.y, 12)
        self.assertEqual(r_obj.id, 12)

    def test_raises(self):
        with self.assertRaises(TypeError):
            Rectangle('12', 12)
        with self.assertRaises(ValueError):
            Rectangle(0, 12)
        with self.assertRaises(ValueError):
            Rectangle(-2, 12)
        with self.assertRaises(TypeError):
            Rectangle(12, '12')
        with self.assertRaises(ValueError):
            Rectangle(12, 0)
        with self.assertRaises(ValueError):
            Rectangle(12, -10)
        with self.assertRaises(ValueError):
            Rectangle(12, 12, x=-1)
        with self.assertRaises(ValueError):
            Rectangle(12, 12, y=-1)

    def test_area(self):
        r_obj = Rectangle(3, 4)
        self.assertEqual(r_obj.area(), 12)
