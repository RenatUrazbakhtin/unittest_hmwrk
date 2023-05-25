from utils import arrs
import unittest

class TestArss(unittest.TestCase):
    def test_get(self):
        self.assertEquals(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEquals(arrs.get([1, 2, 3], -1, "test"), "test")
        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
