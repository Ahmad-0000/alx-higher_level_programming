import unittest
import os
import json
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_id_0(self):
        s_obj = Square(12, id=-12)
        self.assertEqual(s_obj.id, -12)
        self.assertIs(type(s_obj.id), int)

    def test_id_1(self):
        s_obj = Square(1, id=12)
        self.assertEqual(s_obj.id, 12)
        self.assertIs(type(s_obj.id), int)

    def test_id_2(self):
        s_obj = Square(12, id=12.12)
        self.assertAlmostEqual(s_obj.id, 12.12)
        self.assertIs(type(s_obj.id), float)

    def test_id_3(self):
        s_obj = Square(12, id='12')
        self.assertEqual(s_obj.id, '12')
        self.assertIs(type(s_obj.id), str)

    def test_id_4(self):
        s_obj = Square(12, id=None)
        self.assertNotEqual(s_obj.id, None)
        self.assertIs(type(s_obj.id), int)

    def test_id_5(self):
        s_obj = Square(12, id=True)
        self.assertEqual(s_obj.id, True)
        self.assertIs(type(s_obj.id), bool)

    def test_id_6(self):
        s_obj = Square(12, id=[12])
        self.assertEqual(s_obj.id, [12])
        self.assertIs(type(s_obj.id), list)

    def test_id_7(self):
        s_obj = Square(12, id={'12':12})
        self.assertEqual(s_obj.id, {'12':12})
        self.assertIs(type(s_obj.id), dict)

    def test_id_8(self):
        s_obj = Square(12, id=(12,))
        self.assertEqual(s_obj.id, (12,))
        self.assertIs(type(s_obj.id), tuple)

    def test_id_9(self):
        s_obj = Square(12, id={12, 13})
        self.assertEqual(s_obj.id, {12, 13})
        self.assertIs(type(s_obj.id), set)

    def test_id_10(self):
        s_obj = Square(1, id=12j+12)
        self.assertEqual(s_obj.id, 12j+12)
        self.assertIs(type(s_obj.id), complex)

    def test_size(self):
        s_obj = Square(12)
        self.assertEqual(s_obj.size, 12)
        self.assertIs(type(s_obj.size), int)
        self.assertEqual(s_obj.x, 0)
        self.assertIs(type(s_obj.x), int)
        self.assertEqual(s_obj.y, 0)
        self.assertIs(type(s_obj.y), int)

    def test_size_raises(self):
        self.assertRaises(TypeError, Square, 12.12)
        self.assertRaises(TypeError, Square, '12')
        self.assertRaises(TypeError, Square, True)
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, [])
        self.assertRaises(TypeError, Square, {})
        self.assertRaises(TypeError, Square, (1,))
        self.assertRaises(TypeError, Square, {1,2})
        self.assertRaises(TypeError, Square, 12j+12)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -12)

    def test_x(self):
        s_obj = Square(5)
        self.assertEqual(s_obj.x, 0)
        self.assertIs(type(s_obj.x), int)
        s_obj = Square(5, x=12)
        self.assertEqual(s_obj.x, 12)
        self.assertIs(type(s_obj.x), int)

    def test_x_raises(self):
        self.assertRaises(TypeError, Square, 12, 12.12)
        self.assertRaises(TypeError, Square, 12, '12')
        self.assertRaises(TypeError, Square, 12, True)
        self.assertRaises(TypeError, Square, 12, None)
        self.assertRaises(TypeError, Square, 12, [])
        self.assertRaises(TypeError, Square, 12, {})
        self.assertRaises(TypeError, Square, 12, (1,))
        self.assertRaises(TypeError, Square, 12, {1,2})
        self.assertRaises(TypeError, Square, 12, 12j+12)
        self.assertRaises(ValueError, Square, 12, -12)

    def test_y(self):
        s_obj = Square(5)
        self.assertEqual(s_obj.y, 0)
        self.assertIs(type(s_obj.y), int)
        s_obj = Square(5, y=12)
        self.assertEqual(s_obj.y, 12)
        self.assertIs(type(s_obj.y), int)

    def test_y_raises(self):
        self.assertRaises(TypeError, Square, 12, 12, 12.12)
        self.assertRaises(TypeError, Square, 12, 12, '12')
        self.assertRaises(TypeError, Square, 12, 12, True)
        self.assertRaises(TypeError, Square, 12, 12, None)
        self.assertRaises(TypeError, Square, 12, 12, [])
        self.assertRaises(TypeError, Square, 12, 12, {})
        self.assertRaises(TypeError, Square, 12, 12, (1,))
        self.assertRaises(TypeError, Square, 12, 12, {1,2})
        self.assertRaises(TypeError, Square, 12, 12, 12j+12)
        self.assertRaises(ValueError, Square, 12, 12, -12)

    def test_area(self):
        s_obj = Square(12)
        self.assertEqual(s_obj.area(), 144)
        self.assertIs(type(s_obj.area()), int)
        s_obj = Square(5)
        self.assertEqual(s_obj.area(), 25)
        self.assertIs(type(s_obj.area()), int)

    def test___str__(self):
        s_obj = Square(6, id=12)
        self.assertEqual(s_obj.__str__(), '[Square] (12) 0/0 - 6')
        self.assertIs(type(s_obj.__str__()), str)
        s_obj = Square(6, 12, 12, id=12)
        self.assertEqual(s_obj.__str__(), '[Square] (12) 12/12 - 6')
        self.assertIs(type(s_obj.__str__()), str)

    def test_update_args_1(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1)
        self.assertEqual(s_obj.id, 1)
        self.assertIs(type(s_obj.id), int)
        self.assertEqual(s_obj.size, 12)
        self.assertIs(type(s_obj.size), int)
        self.assertEqual(s_obj.x, 12)
        self.assertIs(type(s_obj.x), int)
        self.assertEqual(s_obj.y, 12)
        self.assertIs(type(s_obj.y), int)

    def test_update_args_2(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1, 2)
        self.assertEqual(s_obj.id, 1)
        self.assertIs(type(s_obj.id), int)
        self.assertEqual(s_obj.size, 2)
        self.assertIs(type(s_obj.size), int)
        self.assertEqual(s_obj.x, 12)
        self.assertIs(type(s_obj.x), int)
        self.assertEqual(s_obj.y, 12)
        self.assertIs(type(s_obj.y), int)

    def test_update_args_3(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1, 2, 3)
        self.assertEqual(s_obj.id, 1)
        self.assertIs(type(s_obj.id), int)
        self.assertEqual(s_obj.size, 2)
        self.assertIs(type(s_obj.size), int)
        self.assertEqual(s_obj.x, 3)
        self.assertIs(type(s_obj.x), int)
        self.assertEqual(s_obj.y, 12)
        self.assertIs(type(s_obj.y), int)

    def test_update_args_4(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(1, 2, 3, 4)
        self.assertEqual(s_obj.id, 1)
        self.assertIs(type(s_obj.id), int)
        self.assertEqual(s_obj.size, 2)
        self.assertIs(type(s_obj.size), int)
        self.assertEqual(s_obj.x, 3)
        self.assertIs(type(s_obj.x), int)
        self.assertEqual(s_obj.y, 4)
        self.assertIs(type(s_obj.y), int)

    def test_kwargs_0(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(24, 24, 24, 24, id=48, size=48, x=48, y=48)
        self.assertEqual(s_obj.id, 24)
        self.assertIs(type(s_obj.id), int)
        self.assertEqual(s_obj.size, 24)
        self.assertIs(type(s_obj.size), int)
        self.assertEqual(s_obj.x, 24)
        self.assertIs(type(s_obj.x), int)
        self.assertEqual(s_obj.y, 24)
        self.assertIs(type(s_obj.y), int)

    def test_kwargs_1(self):
        s_obj = Square(12, 12, 12, 12)
        s_obj.update(id=48, size=48, x=48, y=48)
        self.assertEqual(s_obj.id, 48)
        self.assertIs(type(s_obj.id), int)
        self.assertEqual(s_obj.size, 48)
        self.assertIs(type(s_obj.size), int)
        self.assertEqual(s_obj.x, 48)
        self.assertIs(type(s_obj.x), int)
        self.assertEqual(s_obj.y, 48)
        self.assertIs(type(s_obj.y), int)

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
        self.assertRaises(TypeError, s_obj.update, 12, 12j+12)
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
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12j+12)
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
        self.assertRaises(TypeError, s_obj.update, 12, 12, 12, 12j+12)
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
        self.assertRaises(TypeError, s_obj.update, size=12j+12)
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
        self.assertRaises(TypeError, s_obj.update, x=12j+12)
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
        self.assertRaises(TypeError, s_obj.update, y=12j+12)
        self.assertRaises(ValueError, s_obj.update, y=-1)

    def test_to_dictionary_method_1(self):
        s_obj = Square(12, id=15)
        hard_dict_repr = {'size':12, 'x':0, 'y':0, 'id':15}
        dict_repr = s_obj.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr, hard_dict_repr)

    def test_to_dictionary_method_2(self):
        s_obj = Square(12, 13, id=15)
        hard_dict_repr = {'size':12, 'x':13, 'y':0, 'id':15}
        dict_repr = s_obj.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr, hard_dict_repr)

    def test_to_dictionary_method_3(self):
        s_obj = Square(12, 13, 14, id=15)
        hard_dict_repr = {'size':12, 'x':13, 'y':14, 'id':15}
        dict_repr = s_obj.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        self.assertEqual(dict_repr, hard_dict_repr)

    def test_to_json_string_method_Rectangle(self):
        s = Square(12, 12, 12, 12)
        dict_repr = s.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        json_repr = s.to_json_string([dict_repr])
        self.assertEqual(json_repr, '[{"id": 12, "x": 12, "size": 12, "y": 12}]')
        self.assertIs(type(json_repr), str)

    def test_to_json_string_method_empty(self):
        dict_repr = {}
        self.assertIs(type(dict_repr), dict)
        json_repr = Square.to_json_string(dict_repr)
        self.assertIs(type(json_repr), str)
        self.assertEqual(json_repr, '"[]"')

    def test_to_json_string_method_None(self):
        dict_repr = None
        self.assertIs(type(dict_repr), type(None))
        json_repr = Square.to_json_string(dict_repr)
        self.assertIs(type(json_repr), str)
        self.assertEqual(json_repr, '"[]"')

    def test_save_to_file_method_0(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", 'r', encoding='utf') as my_file:
            exp_output = json.dumps([s1.to_dictionary(), s2.to_dictionary()])
            self.assertEqual(my_file.read(), exp_output)

    def test_save_to_file_method_1(self):
        s3 = Square(14, 74, 122, 38)
        s4 = Square(62, 45)
        Square.save_to_file([s3, s4])
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", 'r', encoding='utf') as my_file:
            exp_output = json.dumps([s3.to_dictionary(), s4.to_dictionary()])
            self.assertEqual(my_file.read(), exp_output)

    def test_save_to_file_method_2(self):
        Square.save_to_file([])
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", 'r', encoding='utf') as my_file:
            exp_output = '"[]"'
            self.assertEqual(my_file.read(), exp_output)

    def test_save_to_file_method_3(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", 'r', encoding='utf') as my_file:
            exp_output = '"[]"'
            self.assertEqual(my_file.read(), exp_output)

    def test_form_josn_string_method_0(self):
        s = Square(12, 12, 12, 12)
        json_string = json.dumps(s.to_dictionary())
        from_json = Square.from_json_string(json_string)
        self.assertEqual(from_json, s.to_dictionary())
        self.assertIs(type(from_json), dict)

    def test_form_josn_string_method_1(self):
        json_string = json.dumps([])
        from_json = Square.from_json_string(json_string)
        self.assertEqual(from_json, [])
        self.assertIs(type(from_json), list)

    def test_form_josn_string_method_2(self):
        from_json = Square.from_json_string(None)
        self.assertEqual(from_json, [])
        self.assertIs(type(from_json), list)
