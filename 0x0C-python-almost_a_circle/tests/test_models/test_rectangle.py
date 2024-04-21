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
        self.assertRaises(TypeError, Rectangle, (1,), 12)
        self.assertRaises(TypeError, Rectangle, {1, 2}, 12)
        self.assertRaises(ValueError, Rectangle, 0, 12)
        self.assertRaises(ValueError, Rectangle, -12, 12)

    def test_height(self):
        self.assertEqual(Rectangle(12, 13).height, 13)

    def test_height_raises(self):
        self.assertRaises(TypeError, Rectangle, 12, 12.12)
        self.assertRaises(TypeError, Rectangle, 12, "12")
        self.assertRaises(TypeError, Rectangle, 12, True)
        self.assertRaises(TypeError, Rectangle, 12, None)
        self.assertRaises(TypeError, Rectangle, 12, [])
        self.assertRaises(TypeError, Rectangle, 12, {})
        self.assertRaises(TypeError, Rectangle, 12, (1,))
        self.assertRaises(TypeError, Rectangle, 12, {1, 2})
        self.assertRaises(ValueError, Rectangle, 12, 0)
        self.assertRaises(ValueError, Rectangle, 12, -12)

    def test_x(self):
        self.assertEqual(Rectangle(12, 12).x, 0)
        self.assertEqual(Rectangle(12, 12, 13).x, 13)

    def test_x_raises(self):
        self.assertRaises(TypeError, Rectangle, 12, 12, 12.12)
        self.assertRaises(TypeError, Rectangle, 12, 12, "12")
        self.assertRaises(TypeError, Rectangle, 12, 12, True)
        self.assertRaises(TypeError, Rectangle, 12, 12, None)
        self.assertRaises(TypeError, Rectangle, 12, 12, [])
        self.assertRaises(TypeError, Rectangle, 12, 12, {})
        self.assertRaises(TypeError, Rectangle, 12, 12, (1,))
        self.assertRaises(TypeError, Rectangle, 12, 12, {1,2})
        self.assertRaises(ValueError, Rectangle, 12, 12, -1)

    def test_y(self):
        self.assertEqual(Rectangle(12, 12, 12).y, 0)
        self.assertEqual(Rectangle(12, 12, 12, 13).y, 13)

    def test_x_raises(self):
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, 12.12)
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, "12")
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, True)
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, None)
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, [])
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, {})
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, (1,))
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, {1,2})
        self.assertRaises(ValueError, Rectangle, 12, 12, 12, -1)

    def test_area(self):
        self.assertEqual(Rectangle(12, 12).area(), 144)

    def test_str_special(self):
        self.assertEqual(Rectangle(12, 13, 14, 15, 16).__str__(), '[Rectangle] (16) 14/15 - 12/13')

    def test_update_1(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)
        r.update(1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)
    
    def test_update_2(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)
        r.update(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)

    def test_update_3(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)
        r.update(1, 2, 3)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)


    def test_update_4(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)
        r.update(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 12)

    def test_update_5(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_1_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, "12")
        self.assertRaises(TypeError, r.update, 12, True)
        self.assertRaises(TypeError, r.update, 12, None)
        self.assertRaises(TypeError, r.update, 12, [])
        self.assertRaises(TypeError, r.update, 12, {})
        self.assertRaises(TypeError, r.update, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, {1,2})
        self.assertRaises(ValueError, r.update, 12, 0)
        self.assertRaises(ValueError, r.update, 12, -1)

    def test_update_2_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, 12, '12')
        self.assertRaises(TypeError, r.update, 12, 12, True)
        self.assertRaises(TypeError, r.update, 12, 12, None)
        self.assertRaises(TypeError, r.update, 12, 12, [])
        self.assertRaises(TypeError, r.update, 12, 12, {})
        self.assertRaises(TypeError, r.update, 12, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, 12, {1, 2})
        self.assertRaises(ValueError, r.update, 12, 12, 0)
        self.assertRaises(ValueError, r.update, 12, 12, -12)

    def test_update_3_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, '12')
        self.assertRaises(TypeError, r.update, 12, 12, 12, True)
        self.assertRaises(TypeError, r.update, 12, 12, 12, None)
        self.assertRaises(TypeError, r.update, 12, 12, 12, [])
        self.assertRaises(TypeError, r.update, 12, 12, 12, {})
        self.assertRaises(TypeError, r.update, 12, 12, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, 12, 12, {1, 2})
        self.assertRaises(ValueError, r.update, 12, 12, 12, -12)

    def test_update_4_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, '12')
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, True)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, None)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, [])
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, {})
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, {1, 2})
        self.assertRaises(ValueError, r.update, 12, 12, 12, 12, -12)
