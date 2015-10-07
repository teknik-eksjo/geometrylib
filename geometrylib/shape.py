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
        return ((self.a, self.b, self.c),
                (self.b, self.c, self.a),
                (self.c, self.a, self.b))

    def __eq__(self, other):
        """Returns whether this triangle equals another triangle."""
        sides = (self.a, self.b, self.c)
        return any(sides == rotation for rotation in other._rotations())

    def is_similar(self, triangle):
        """Return whether this triangle is similar to another triangle."""
        return any(self.a / a == self.b / b == self.c / c for a, b, c in triangle._rotations())

    def is_equilateral(self):
        """Return whether this triangle is equilateral."""
        return self.a == self.b == self.c

    def is_isosceles(self):
        """Return wheter this triangle is isosceles."""
        return any(a == b for a, b, c in self._rotations())

    def perimeter(self):
        """Return the perimiter of the triangle."""
        return self.a + self.b + self.c

    def area(self):
        """Return the area of this triangle."""
        s = (self.a + self.b + self.c)/2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def scale(self, factor):
        """Return a new triangle, `factor` times the size of this one."""
        return Triangle(self.a * factor, self.b * factor, self.c * factor)
