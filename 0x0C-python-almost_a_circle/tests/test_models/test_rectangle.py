import unittest
import os
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_id_0(self):
        r = Rectangle(1, 1, id=-12)
        self.assertEqual(r.id, -12)
        self.assertIs(type(r.id), int)

    def test_id_1(self):
        r = Rectangle(1, 1, id=12)
        self.assertEqual(r.id, 12)
        self.assertIs(type(r.id), int)
    
    def test_id_2(self):
        r = Rectangle(1, 1, id=12.12)
        self.assertAlmostEqual(r.id, 12.12)
        self.assertIs(type(r.id), float)

    def test_id_3(self):
        r = Rectangle(1, 1, id='12')
        self.assertEqual(r.id, '12')
        self.assertIs(type(r.id), str)


    def test_id_4(self):
        r = Rectangle(1, 1, id=None)
        self.assertNotEqual(r.id, None)
        self.assertIs(type(r.id), int)

    def test_id_5(self):
        r = Rectangle(1, 1, id=True)
        self.assertEqual(r.id, True)
        self.assertIs(type(r.id), bool)

    def test_id_6(self):
        r = Rectangle(1, 1, id=[12])
        self.assertEqual(r.id, [12])
        self.assertIs(type(r.id), list)

    def test_id_7(self):
        r = Rectangle(1, 1, id={'12':12})
        self.assertEqual(r.id, {'12':12})
        self.assertIs(type(r.id), dict)

    def test_id_8(self):
        r = Rectangle(1, 1, id=(12,))
        self.assertEqual(r.id, (12,))
        self.assertIs(type(r.id), tuple)

    def test_id_9(self):
        r = Rectangle(1, 1, id={12, 13})
        self.assertEqual(r.id, {12, 13})
        self.assertEqual(type(r.id), set)
    
    def test_id_10(self):
        r = Rectangle(1, 1, id=12j+12)
        self.assertEqual(r.id, 12j+12)
        self.assertEqual(type(r.id), complex)

    def test_width(self):
        r = Rectangle(12, 13)
        self.assertEqual(r.width, 12)
        self.assertIs(type(r.width), int)

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
        r = Rectangle(12, 13)
        self.assertEqual(r.height, 13)
        self.assertIs(type(r.height), int)

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
        r = Rectangle(12, 12)
        self.assertEqual(r.x, 0)
        self.assertIs(type(r.x), int)
        r = Rectangle(12, 12, 13)
        self.assertEqual(r.x, 13)
        self.assertIs(type(r.x), int)

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
        r = Rectangle(12, 12, 12)
        self.assertEqual(r.y, 0)
        self.assertIs(type(r.y), int)
        r = Rectangle(12, 12, 12, 13)
        self.assertEqual(r.y, 13)
        self.assertIs(type(r.y), int)

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
        r = Rectangle(12, 12)
        self.assertEqual(r.area(), 144)
        self.assertIs(type(r.area()), int)
        r = Rectangle(6, 5)
        self.assertEqual(r.area(), 30)

    def test_str_special(self):
        r = Rectangle(12, 13, 14, 15, 16)
        self.assertEqual(r.__str__(), '[Rectangle] (16) 14/15 - 12/13')
        self.assertIs(type(r.__str__()), str)

    def test_update_args_1(self):
        r = Rectangle(12, 12, 12, 12, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 12)
        r.update(1)
        self.assertEqual(r.id, 1)
        self.assertIs(type(r.id), int)
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
        self.assertIs(type(r.id), int)
        self.assertEqual(r.width, 2)
        self.assertIs(type(r.width), int)
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
        self.assertIs(type(r.id), int)
        self.assertEqual(r.width, 2)
        self.assertIs(type(r.width), int)
        self.assertEqual(r.height, 3)
        self.assertIs(type(r.height), int)
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
        self.assertIs(type(r.id), int)
        self.assertEqual(r.width, 2)
        self.assertIs(type(r.width), int)
        self.assertEqual(r.height, 3)
        self.assertIs(type(r.height), int)
        self.assertEqual(r.x, 4)
        self.assertIs(type(r.x), int)
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
        self.assertIs(type(r.id), int)
        self.assertEqual(r.width, 2)
        self.assertIs(type(r.width), int)
        self.assertEqual(r.height, 3)
        self.assertIs(type(r.height), int)
        self.assertEqual(r.x, 4)
        self.assertIs(type(r.x), int)
        self.assertEqual(r.y, 5)
        self.assertIs(type(r.y), int)

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
        self.assertIs(type(r.id), int)
        self.assertEqual(r.width, 12)
        self.assertIs(type(r.width), int)
        self.assertEqual(r.height, 12)
        self.assertIs(type(r.height), int)
        self.assertEqual(r.x, 12)
        self.assertIs(type(r.x), int)
        self.assertEqual(r.y, 12)
        self.assertIs(type(r.y), int)

    def test_update_kwargs_2(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=12, width=12, height=12, x=12, y=12)
        self.assertEqual(r.id, 12)
        self.assertIs(type(r.id), int)
        self.assertEqual(r.width, 12)
        self.assertIs(type(r.width), int)
        self.assertEqual(r.height, 12)
        self.assertIs(type(r.height), int)
        self.assertEqual(r.x, 12)
        self.assertIs(type(r.x), int)
        self.assertEqual(r.y, 12)
        self.assertIs(type(r.y), int)

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

    def test_to_json_string_method_Rectangle(self):
        r = Rectangle(12, 12, 12, 12, 12)
        dict_repr = r.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        json_repr = r.to_json_string([dict_repr])
        self.assertEqual(json_repr, '[{"x": 12, "y": 12, "id": 12, "height": 12, "width": 12}]')
        self.assertIs(type(json_repr), str)

    def test_to_json_string_method_empty(self):
        dict_repr = {}
        self.assertIs(type(dict_repr), dict)
        json_repr = Rectangle.to_json_string(dict_repr)
        self.assertIs(type(json_repr), str)
        self.assertEqual(json_repr, '"[]"')

    def test_to_json_string_method_None(self):
        dict_repr = None
        self.assertIs(type(dict_repr), type(None))
        json_repr = Rectangle.to_json_string(dict_repr)
        self.assertIs(type(json_repr), str)
        self.assertEqual(json_repr, '"[]"')

    def test_save_to_file_method_0(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf') as my_file:
            exp_output = json.dumps([r1.to_dictionary(), r2.to_dictionary()])
            self.assertEqual(my_file.read(), exp_output)

    def test_save_to_file_method_1(self):
        r3 = Rectangle(15, 20, 14, 9)
        r4 = Rectangle(7, 19)
        Rectangle.save_to_file([r3, r4])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf') as my_file:
            exp_output = json.dumps([r3.to_dictionary(), r4.to_dictionary()])
            self.assertEqual(my_file.read(), exp_output)
    
    def test_save_to_file_method_2(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf') as my_file:
            exp_output = '"[]"'
            self.assertEqual(my_file.read(), exp_output)

    def test_save_to_file_method_3(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf') as my_file:
            exp_output = '"[]"'
            self.assertEqual(my_file.read(), exp_output)

    def test_form_josn_string_method_0(self):
        r1 = Rectangle(12, 12, 12, 12)
        json_string = json.dumps(r1.to_dictionary())
        from_json = Rectangle.from_json_string(json_string)
        self.assertEqual(from_json, r1.to_dictionary())
        self.assertIs(type(from_json), dict)

    def test_form_josn_string_method_1(self):
        json_string = json.dumps([])
        from_json = Rectangle.from_json_string(json_string)
        self.assertEqual(from_json, [])
        self.assertIs(type(from_json), list)

    def test_form_josn_string_method_2(self):
        from_json = Rectangle.from_json_string(None)
        self.assertEqual(from_json, [])
        self.assertIs(type(from_json), list)

    def test_create_method(self):
        r1 = Rectangle(12, 12, 12, 12)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        r2_dict = r2.to_dictionary()
        self.assertEqual(r1_dict, r2_dict)
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)
        self.assertIsInstance(r2, Rectangle)

    def test_load_from_file_exists(self):
        filename = "Rectangle.json"
        r1 = Rectangle(12, 12, 12, 12)
        r2 = Rectangle(24, 24, 24, 24)
        r3 = Rectangle(48, 48, 48, 48)
        Rs_list_input = [r1, r2, r3]
        Rectangle.save_to_file(Rs_list_input)
        Rs_list_output = Rectangle.load_from_file()
        for obj in Rs_list_output:
            with self.subTest(obj=obj):
                self.assertIsInstance(obj, Rectangle)

    def test_load_from_file_not_exists(self):
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        Rs_list_output = Rectangle.load_from_file()
        self.assertEqual(len(Rs_list_output), 0)
        self.assertIs(type(Rs_list_output), list)
