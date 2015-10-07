"""Use the triangle class to represent triangles."""

from math import sqrt

class Triangle():
    """A triangle is a three-sided polygon."""

    def __init__(self, a, b, c):
        """Create a triangle with sides of length `a`, `b` and `c`.

        Raises `ValueError` if the three sides cannot form a triangle.

        """
        self.a, self.b, self.c = float(a), float(b), float(c)
        if any(s <= 0 for s in (a, b, c)):
            raise ValueError('side lengths must all be positive')
        if any(a >= b + c for a, b, c in self._rotations()):
            raise ValueError('one side is too long to make a triangle')

    def _rotations(self):
        """Return each of the three ways of rotating our sides."""
        return False

    def __eq__(self, other):
        """Returns whether this triangle equals another triangle."""
        return False

    def is_similar(self, triangle):
        """Return whether this triangle is similar to another triangle."""
        return False

    def is_equilateral(self):
        """Return whether this triangle is equilateral."""
        return False

    def is_isosceles(self):
        """Return wheter this triangle is isosceles."""
        return False

    def perimeter(self):
        """Return the perimiter of the triangle."""
        return False

    def area(self):
        """Return the area of this triangle."""
        return 0.0

    def scale(self, factor):
        """Return a new triangle, `factor` times the size of this one."""
        return self
