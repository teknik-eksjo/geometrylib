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
        t1 = Triangle(2, 3, 4)
        t2 = Triangle(2, 3, 4)
        t3 = Triangle(3, 4, 2)
        t4 = Triangle(3, 2, 4)

        self.assertEqual(t1, t2)
        self.assertEqual(t1, t3)
        self.assertEqual(t2, t3)
        self.assertNotEqual(t1, t4)

    def test_is_similar(self):
        t = Triangle(4, 6, 7)
        self.assertTrue(t.is_similar(Triangle(8, 12, 14)))
        self.assertFalse(t.is_similar(Triangle(8, 12, 12)))

    def test_is_equilateral(self):
        self.assertTrue(Triangle(4, 4, 4).is_equilateral())
        self.assertFalse(Triangle(4, 4, 5).is_equilateral())

    def test_is_isosceles(self):
        self.assertTrue(Triangle(4, 4, 5).is_isosceles())
        self.assertTrue(Triangle(4, 4, 4).is_isosceles())
        self.assertFalse(Triangle(4, 5, 6).is_isosceles())

    def test_perimeter(self):
        self.assertEqual(Triangle(4, 5, 6).perimeter(), 15)
        self.assertNotEqual(Triangle(4, 5, 8).perimeter(), 15)

    def test_area(self):
        self.assertEqual(Triangle(3, 4, 5).area(), 6)
        self.assertNotEqual(Triangle(3, 4, 2).area(), 6)

    def test_scale(self):
        t = Triangle(4, 5, 6)
        self.assertEqual(t.scale(2), Triangle(8, 10, 12))
        self.assertEqual(t.scale(2), Triangle(12, 8, 10))
        self.assertNotEqual(t.scale(2), Triangle(10, 10, 12))
