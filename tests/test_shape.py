import unittest
from geometrylib.shape import Triangle

class TriangleTests(unittest.TestCase):

    def test_raises_valueerror(self):
        self.assertRaises(ValueError, Triangle, 2, 3, 10)
        self.assertRaises(ValueError, Triangle, 2, 3, -4)

    def test_rotations(self):
        t1 = Triangle(3, 4, 5)
        self.assertEqual(t1._rotations(), ((3, 4, 5),
                                           (4, 5, 3),
                                           (5, 3, 4)))

    def test_equal(self):
        pass

    def test_is_similar(self):
        pass

    def test_is_equilateral(self):
        pass

    def test_is_isosceles(self):
        pass

    def test_perimeter(self):
        pass

    def test_area(self):
        pass

    def test_scale(self):
        pass
