import unittest
from geometrylib import utils

class TestUtils(unittest.TestCase):

    def test_is_triangle(self):
        self.assertTrue(utils.is_triangle(4, 5, 6))
        self.assertFalse(utils.is_triangle(10, 20, 50))

    def test_is_equilateral(self):
        self.assertFalse(utils.is_equilateral(4, 5, 6))
        self.assertFalse(utils.is_equilateral(4, 5, 60))
        self.assertTrue(utils.is_equilateral(6, 6, 6))

    def test_is_isosceles(self):
        self.assertFalse(utils.is_isosceles(6, 6, 30))
        self.assertFalse(utils.is_isosceles(4, 5, 6))
        self.assertTrue(utils.is_isosceles(7, 7, 8))

    def test_compute_perimiter(self):
        self.assertEqual(utils.compute_perimiter(4, 5, 50), 0)
        self.assertEqual(utils.compute_perimiter(4, 5, 6), 15)
        self.assertEqual(utils.compute_perimiter(8, 10, 8), 26)

    def test_compute_area(self):
        self.assertEqual(utils.compute_area(8, 8, 80), 0)
        self.assertEqual(utils.compute_area(3, 4, 5), 6)
        self.assertEqual(utils.compute_area(30, 40, 50), 600)
