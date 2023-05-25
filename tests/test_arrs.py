from utils import arrs
import unittest

class TestArss(unittest.TestCase):
    def test_get(self):
        self.assertEquals(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEquals(arrs.get([1, 2, 3], -1, "test"), "test")
        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")

class TestSlice(unittest.TestCase):
    def test_slice(self):
        self.assertEquals(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEquals(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEquals(arrs.my_slice([1, 2, 3, 4], -3, 2), [2])
        self.assertEquals(arrs.my_slice([1, 2, 3], -4, 1), [1])
        self.assertEquals(arrs.my_slice([], 1), [])