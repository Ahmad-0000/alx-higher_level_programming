import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_id(self):
        self.assertEqual(Square(5, id=12).id, 12)

    def test_size(self):
        s_obj = Square(12)
        self.assertEqual(s_obj.size, 12)
        self.assertEqual(s_obj.x, 0)
        self.assertEqual(s_obj.y, 0)

    def test_size_raises(self):
        self.assertRaises(TypeError, Square, 12.12)
        self.assertRaises(TypeError, Square, '12')
        self.assertRaises(TypeError, Square, True)
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, [])
        self.assertRaises(TypeError, Square, {})
        self.assertRaises(TypeError, Square, (1,))
        self.assertRaises(TypeError, Square, {1,2})
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -12)

    def test_x(self):
        self.assertEqual(Square(5).x, 0)
        self.assertEqual(Square(5, x=12).x, 12)

    def test_x_raises(self):
        self.assertRaises(TypeError, Square, 12, 12.12)
        self.assertRaises(TypeError, Square, 12, '12')
        self.assertRaises(TypeError, Square, 12, True)
        self.assertRaises(TypeError, Square, 12, None)
        self.assertRaises(TypeError, Square, 12, [])
        self.assertRaises(TypeError, Square, 12, {})
        self.assertRaises(TypeError, Square, 12, (1,))
        self.assertRaises(TypeError, Square, 12, {1,2})
        self.assertRaises(ValueError, Square, 12, -12)

    def test_y(self):
        self.assertEqual(Square(5).y, 0)
        self.assertEqual(Square(5, y=12).y, 12)

    def test_y_raises(self):
        self.assertRaises(TypeError, Square, 12, 12, 12.12)
        self.assertRaises(TypeError, Square, 12, 12, '12')
        self.assertRaises(TypeError, Square, 12, 12, True)
        self.assertRaises(TypeError, Square, 12, 12, None)
        self.assertRaises(TypeError, Square, 12, 12, [])
        self.assertRaises(TypeError, Square, 12, 12, {})
        self.assertRaises(TypeError, Square, 12, 12, (1,))
        self.assertRaises(TypeError, Square, 12, 12, {1,2})
        self.assertRaises(ValueError, Square, 12, 12, -12)

    def test___str__(self):
        self.assertEqual(Square(6, id=12).__str__(), '[Square] (12) 0/0 - 6')
        self.assertEqual(Square(6, 12, 12, id=12).__str__(), '[Square] (12) 12/12 - 6')
