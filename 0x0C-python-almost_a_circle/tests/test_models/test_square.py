import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_id(self):
        self.assertEqual(Square(5, id=12).id, 12)

    def test_size(self):
        self.assertEqual(Square(12).size, 12)

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
