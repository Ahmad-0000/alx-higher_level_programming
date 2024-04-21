import unittest
from models.base import Base

class TestId(unittest.TestCase):
    def test_id(self):
        temp_obj = Base()
        self.assertEqual(temp_obj.id, 1)
        temp_obj = Base(12)
        self.assertEqual(temp_obj.id, 12)
