import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_id_1(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_2(self):
        b = Base(id=12.12)
        self.assertAlmostEqual(b.id, 12.12)

    def test_id_3(self):
        b = Base(id='12')
        self.assertEqual(b.id, '12')

    def test_id_4(self):
        b = Base(id=None)
        self.assertNotEqual(b.id, None)

    def test_id_5(self):
        b = Base(id=True)
        self.assertEqual(b.id, True)

    def test_id_6(self):
        b = Base(id=[12])
        self.assertEqual(b.id, [12])

    def test_id_7(self):
        b = Base(id={'12':12})
        self.assertEqual(b.id, {'12':12})

    def test_id_8(self):
        b = Base(id=(12,))
        self.assertEqual(b.id, (12,))

    def test_id_9(self):
        b = Base(id={12, 13})
        self.assertEqual(b.id, {12, 13})
