import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        self.assertIs(type(b.id), int)
        b = Base()
        self.assertEqual(b.id, 2)
        self.assertIs(type(b.id), int)

    def test_id_0(self):
        b = Base(id=-12)
        self.assertEqual(b.id, -12)
        self.assertIs(type(b.id), int)

    def test_id_1(self):
        b = Base(12)
        self.assertEqual(b.id, 12)
        self.assertIs(type(b.id), int)

    def test_id_2(self):
        b = Base(id=12.12)
        self.assertAlmostEqual(b.id, 12.12)
        self.assertIs(type(b.id), float)

    def test_id_3(self):
        b = Base(id='12')
        self.assertEqual(b.id, '12')
        self.assertIs(type(b.id), str)

    def test_id_4(self):
        b = Base(id=None)
        self.assertNotEqual(b.id, None)
        self.assertIs(type(b.id), int)

    def test_id_5(self):
        b = Base(id=True)
        self.assertEqual(b.id, True)
        self.assertIs(type(b.id), bool)

    def test_id_6(self):
        b = Base(id=[12])
        self.assertEqual(b.id, [12])
        self.assertIs(type(b.id), list)

    def test_id_7(self):
        b = Base(id={'12':12})
        self.assertEqual(b.id, {'12':12})
        self.assertIs(type(b.id), dict)

    def test_id_8(self):
        b = Base(id=(12,))
        self.assertEqual(b.id, (12,))
        self.assertIs(type(b.id), tuple)

    def test_id_9(self):
        b = Base(id={12, 13})
        self.assertEqual(b.id, {12, 13})
        self.assertIs(type(b.id), set)

    def test_id_10(self):
        b = Base(id=12j+12)
        self.assertEqual(b.id, 12j+12)
        self.assertIs(type(b.id), complex)

    def test_to_json_string_method_Rectangle(self):
        r = Rectangle(12, 12, 12, 12, 12)
        dict_repr = r.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        json_repr = r.to_json_string([dict_repr])
        self.assertEqual(json_repr, '[{"x": 12, "y": 12, "id": 12, "height": 12, "width": 12}]')
        self.assertIs(type(json_repr), str)

    def test_to_json_string_method_Square(self):
        s = Square(12, 12, 12, 12)
        dict_repr = s.to_dictionary()
        self.assertIs(type(dict_repr), dict)
        json_repr = s.to_json_string([dict_repr])
        self.assertEqual(json_repr, '[{"id": 12, "x": 12, "size": 12, "y": 12}]')
        self.assertIs(type(json_repr), str)

    def test_to_json_string_method_empty(self):
        dict_repr = {}
        self.assertIs(type(dict_repr), dict)
        json_repr = Base.to_json_string(dict_repr)
        self.assertIs(type(json_repr), str)
        self.assertEqual(json_repr, '"[]"')

    def test_to_json_string_method_None(self):
        dict_repr = None
        self.assertIs(type(dict_repr), type(None))
        json_repr = Base.to_json_string(dict_repr)
        self.assertIs(type(json_repr), str)
        self.assertEqual(json_repr, '"[]"')
