import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(12).id, 12)
