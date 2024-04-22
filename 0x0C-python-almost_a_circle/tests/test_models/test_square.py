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

    def test_area(self):
        self.assertEqual(Square(12).area(), 144)

    def test___str__(self):
        self.assertEqual(Square(6, id=12).__str__(), '[Square] (12) 0/0 - 6')
        self.assertEqual(Square(6, 12, 12, id=12).__str__(), '[Square] (12) 12/12 - 6')

    def test_update_args_1(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1)
        self.assertEqual(s_obj.id, 1)
        self.assertEqual(s_obj.size, 12)
        self.assertEqual(s_obj.x, 12)
        self.assertEqual(s_obj.y, 12)

    def test_update_args_2(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1, 2)
        self.assertEqual(s_obj.id, 1)
        self.assertEqual(s_obj.size, 2)
        self.assertEqual(s_obj.x, 12)
        self.assertEqual(s_obj.y, 12)

    def test_update_args_3(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1, 2, 3)
        self.assertEqual(s_obj.id, 1)
        self.assertEqual(s_obj.size, 2)
        self.assertEqual(s_obj.x, 3)
        self.assertEqual(s_obj.y, 12)

    def test_update_args_4(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1, 2, 3, 4)
        self.assertEqual(s_obj.id, 1)
        self.assertEqual(s_obj.size, 2)
        self.assertEqual(s_obj.x, 3)
        self.assertEqual(s_obj.y, 4)

    def test_kwargs_0(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(24, 24, 24, 24, id=48, size=48, x=48, y=48)
        self.assertEqual(s_obj.id, 24)
        self.assertEqual(s_obj.size, 24)
        self.assertEqual(s_obj.x, 24)
        self.assertEqual(s_obj.y, 24)

    def test_kwargs_1(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(id=48, size=48, x=48, y=48)
        self.assertEqual(s_obj.id, 48)
        self.assertEqual(s_obj.size, 48)
        self.assertEqual(s_obj.x, 48)
        self.assertEqual(s_obj.y, 48)

    def test_update_args_1_raises(self):
        s_obj = Square(12, 12, 12, 12)
        self.assertRaises(TypeError, s_obj.update, 12, 12.12)
        self.assertRaises(TypeError, s_obj.update, 12, '12')
        self.assertRaises(TypeError, s_obj.update, 12, True)
        self.assertRaises(TypeError, s_obj.update, 12, None)
        self.assertRaises(TypeError, s_obj.update, 12, [])
        self.assertRaises(TypeError, s_obj.update, 12, {})
        self.assertRaises(TypeError, s_obj.update, 12, (1,))
        self.assertRaises(TypeError, s_obj.update, 12, {1,2})
        self.assertRaises(ValueError, s_obj.update, 12, 0)
        self.assertRaises(ValueError, s_obj.update, 12, -1)

    def test_update_args_2_raises(self):
        s_obj = Square(12, 12, 12, 12)
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12.12)
        self.assertRaises(TypeError, s_obj.update, 12, 12, '12')
        self.assertRaises(TypeError, s_obj.update, 12, 12, True)
        self.assertRaises(TypeError, s_obj.update, 12, 12, None)
        self.assertRaises(TypeError, s_obj.update, 12, 12, [])
        self.assertRaises(TypeError, s_obj.update, 12, 12, {})
        self.assertRaises(TypeError, s_obj.update, 12, 12, (1,))
        self.assertRaises(TypeError, s_obj.update, 12, 12, {1,2})
        self.assertRaises(ValueError, s_obj.update, 12, 12, -1)

    def test_update_args_3_raises(self):
        s_obj = Square(12, 12, 12, 12)
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, 12.12)
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, '12')
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, True)
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, None)
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, [])
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, {})
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, (1,))
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, {1,2})
        self.assertRaises(ValueError, s_obj.update, 12, 12, 12, -1)

    def test_update_kwargs_size_raises(self):
        s_obj = Square(12, 12, 12, 12)
        self.assertRaises(TypeError, s_obj.update, size=12.12)
        self.assertRaises(TypeError, s_obj.update, size='12')
        self.assertRaises(TypeError, s_obj.update, size=True)
        self.assertRaises(TypeError, s_obj.update, size=None)
        self.assertRaises(TypeError, s_obj.update, size=[])
        self.assertRaises(TypeError, s_obj.update, size={})
        self.assertRaises(TypeError, s_obj.update, size=(1,))
        self.assertRaises(TypeError, s_obj.update, size={1,2})
        self.assertRaises(ValueError, s_obj.update, size=0)
        self.assertRaises(ValueError, s_obj.update, size=-1)

    def test_update_kwargs_x_raises(self):
        s_obj = Square(12, 12, 12, 12)
        self.assertRaises(TypeError, s_obj.update, x=12.12)
        self.assertRaises(TypeError, s_obj.update, x='12')
        self.assertRaises(TypeError, s_obj.update, x=True)
        self.assertRaises(TypeError, s_obj.update, x=None)
        self.assertRaises(TypeError, s_obj.update, x=[])
        self.assertRaises(TypeError, s_obj.update, x={})
        self.assertRaises(TypeError, s_obj.update, x=(1,))
        self.assertRaises(TypeError, s_obj.update, x={1,2})
        self.assertRaises(ValueError, s_obj.update, x=-1)

    def test_update_kwargs_y_raises(self):
        s_obj = Square(12, 12, 12, 12)
        self.assertRaises(TypeError, s_obj.update, y=12.12)
        self.assertRaises(TypeError, s_obj.update, y='12')
        self.assertRaises(TypeError, s_obj.update, y=True)
        self.assertRaises(TypeError, s_obj.update, y=None)
        self.assertRaises(TypeError, s_obj.update, y=[])
        self.assertRaises(TypeError, s_obj.update, y={})
        self.assertRaises(TypeError, s_obj.update, y=(1,))
        self.assertRaises(TypeError, s_obj.update, y={1,2})
        self.assertRaises(ValueError, s_obj.update, y=-1)
