import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_id_0(self):
        r = Rectangle(1, 1, id=-12)
        self.assertEqual(r.id, -12)

    def test_id_1(self):
        r = Rectangle(1, 1, id=12)
        self.assertEqual(r.id, 12)
    
    def test_id_2(self):
        r = Rectangle(1, 1, id=12.12)
        self.assertAlmostEqual(r.id, 12.12)

    def test_id_3(self):
        r = Rectangle(1, 1, id='12')
        self.assertEqual(r.id, '12')

    def test_id_4(self):
        r = Rectangle(1, 1, id=None)
        self.assertNotEqual(r.id, None)

    def test_id_5(self):
        r = Rectangle(1, 1, id=True)
        self.assertEqual(r.id, True)

    def test_id_6(self):
        r = Rectangle(1, 1, id=[12])
        self.assertEqual(r.id, [12])

    def test_id_7(self):
        r = Rectangle(1, 1, id={'12':12})
        self.assertEqual(r.id, {'12':12})

    def test_id_8(self):
        r = Rectangle(1, 1, id=(12,))
        self.assertEqual(r.id, (12,))

    def test_id_9(self):
        r = Rectangle(1, 1, id={12, 13})
        self.assertEqual(r.id, {12, 13})
    
    def test_id_10(self):
        r = Rectangle(1, 1, id=12j+12)
        self.assertEqual(r.id, 12j+12)

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
        self.assertRaises(TypeError, Rectangle, 12j+12, 12)
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
        self.assertRaises(TypeError, Rectangle, 12, 12j+12)
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
        self.assertRaises(TypeError, Rectangle, 12, 12, 12j+12)
        self.assertRaises(ValueError, Rectangle, 12, 12, -1)

    def test_y(self):
        self.assertEqual(Rectangle(12, 12, 12).y, 0)
        self.assertEqual(Rectangle(12, 12, 12, 13).y, 13)

    def test_y_raises(self):
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, 12.12)
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, "12")
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, True)
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, None)
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, [])
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, {})
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, (1,))
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, {1,2})
        self.assertRaises(TypeError, Rectangle, 12, 12, 12, 12j+12)
        self.assertRaises(ValueError, Rectangle, 12, 12, 12, -1)

    def test_area(self):
        self.assertEqual(Rectangle(12, 12).area(), 144)

    def test_str_special(self):
        self.assertEqual(Rectangle(12, 13, 14, 15, 16).__str__(), '[Rectangle] (16) 14/15 - 12/13')

    def test_update_args_1(self):
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
    
    def test_update_args_2(self):
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

    def test_update_args_3(self):
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


    def test_update_4_args(self):
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

    def test_update_5_args(self):
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

    def test_update_args_1_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, "12")
        self.assertRaises(TypeError, r.update, 12, True)
        self.assertRaises(TypeError, r.update, 12, None)
        self.assertRaises(TypeError, r.update, 12, [])
        self.assertRaises(TypeError, r.update, 12, {})
        self.assertRaises(TypeError, r.update, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, {1,2})
        self.assertRaises(TypeError, r.update, 12, 12j+12)
        self.assertRaises(ValueError, r.update, 12, 0)
        self.assertRaises(ValueError, r.update, 12, -1)

    def test_update_args_2_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, 12, '12')
        self.assertRaises(TypeError, r.update, 12, 12, True)
        self.assertRaises(TypeError, r.update, 12, 12, None)
        self.assertRaises(TypeError, r.update, 12, 12, [])
        self.assertRaises(TypeError, r.update, 12, 12, {})
        self.assertRaises(TypeError, r.update, 12, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, 12, {1, 2})
        self.assertRaises(TypeError, r.update, 12, 12, 12j+12)
        self.assertRaises(ValueError, r.update, 12, 12, 0)
        self.assertRaises(ValueError, r.update, 12, 12, -12)

    def test_update_args_3_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, '12')
        self.assertRaises(TypeError, r.update, 12, 12, 12, True)
        self.assertRaises(TypeError, r.update, 12, 12, 12, None)
        self.assertRaises(TypeError, r.update, 12, 12, 12, [])
        self.assertRaises(TypeError, r.update, 12, 12, 12, {})
        self.assertRaises(TypeError, r.update, 12, 12, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, 12, 12, {1, 2})
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12j+12)
        self.assertRaises(ValueError, r.update, 12, 12, 12, -12)

    def test_update_args_4_raises(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, 12.12)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, '12')
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, True)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, None)
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, [])
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, {})
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, (1,))
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, {1, 2})
        self.assertRaises(TypeError, r.update, 12, 12, 12, 12, 12j+12)
        self.assertRaises(ValueError, r.update, 12, 12, 12, 12, -12)

    def test_update_kwargs_1(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(12, 12, 12, 12, 12, id=24, width=24, height=24, x=24, y=24)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)

    def test_update_kwargs_2(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=12, width=12, height=12, x=12, y=12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)

    def test_update_kwargs_width_raises(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertRaises(TypeError, r.update, width=12.12)
        self.assertRaises(TypeError, r.update, width='12')
        self.assertRaises(TypeError, r.update, width=True)
        self.assertRaises(TypeError, r.update, width=None)
        self.assertRaises(TypeError, r.update, width=[])
        self.assertRaises(TypeError, r.update, width={})
        self.assertRaises(TypeError, r.update, width=(1,))
        self.assertRaises(TypeError, r.update, width={1,2})
        self.assertRaises(TypeError, r.update, width=12j+12)
        self.assertRaises(ValueError, r.update, width=0)
        self.assertRaises(ValueError, r.update, width=-12)

    def test_update_kwargs_height_raises(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertRaises(TypeError, r.update, height=12.12)
        self.assertRaises(TypeError, r.update, height='12')
        self.assertRaises(TypeError, r.update, height=True)
        self.assertRaises(TypeError, r.update, height=None)
        self.assertRaises(TypeError, r.update, height=[])
        self.assertRaises(TypeError, r.update, height={})
        self.assertRaises(TypeError, r.update, height=(1,))
        self.assertRaises(TypeError, r.update, height={1,2})
        self.assertRaises(TypeError, r.update, height=12j+12)
        self.assertRaises(ValueError, r.update, height=0)
        self.assertRaises(ValueError, r.update, height=-12)

    def test_update_kwargs_x_raises(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertRaises(TypeError, r.update, x=12.12)
        self.assertRaises(TypeError, r.update, x='12')
        self.assertRaises(TypeError, r.update, x=True)
        self.assertRaises(TypeError, r.update, x=None)
        self.assertRaises(TypeError, r.update, x=[])
        self.assertRaises(TypeError, r.update, x={})
        self.assertRaises(TypeError, r.update, x=(1,))
        self.assertRaises(TypeError, r.update, x={1,2})
        self.assertRaises(TypeError, r.update, x=12j+12)
        self.assertRaises(ValueError, r.update, x=-12)

    def test_update_kwargs_y_raises(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertRaises(TypeError, r.update, y=12.12)
        self.assertRaises(TypeError, r.update, y='12')
        self.assertRaises(TypeError, r.update, y=True)
        self.assertRaises(TypeError, r.update, y=None)
        self.assertRaises(TypeError, r.update, y=[])
        self.assertRaises(TypeError, r.update, y={})
        self.assertRaises(TypeError, r.update, y=(1,))
        self.assertRaises(TypeError, r.update, y={1,2})
        self.assertRaises(TypeError, r.update, y=12j+12)
        self.assertRaises(ValueError, r.update, y=-12)

    def test_to_dictionary_method_1(self):
        r = Rectangle(12, 13, id=16)
        hard_dict_repr = {'width':12, 'height':13, 'x':0, 'y':0, 'id':16}
        dict_repr = r.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr, hard_dict_repr)

    def test_to_dictionary_method_2(self):
        r = Rectangle(12, 13, 14, id=16)
        hard_dict_repr = {'width':12, 'height':13, 'x':14, 'y':0, 'id':16}
        dict_repr = r.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr, hard_dict_repr)

    def test_to_dictionary_method_3(self):
        r = Rectangle(12, 13, 14, 15, id=16)
        hard_dict_repr = {'width':12, 'height':13, 'x':14, 'y':15, 'id':16}
        dict_repr = r.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr, hard_dict_repr)
