"""Routines to test triangle properties without explicit instantiation."""

from geometrylib.shape import Triangle


def _make_triangle(a, b, c):
    try:
        return Triangle(a, b, c)
    except ValueError:
        return None

def is_triangle(a, b, c):
    """Test whether lengths `a`, `b` and `c` can be the sides of a triangle."""
    return False

def is_equilateral(a, b, c):
    """Return whether lengths `a`, `b` and `c` are an equilateral triangle."""
    return False

def is_isosceles(a, b, c):
    """Return whether lengths `a`, `b` and `c` are an isosceles triangle."""
    return False

def compute_perimiter(a, b, c):
    """Return the perimeter of the triangle with side lengths `a`, `b` and `c`.

    If the three lengths provided cannot form a triangle,
    then the perimeter 0.0 is returned.

    """
    return 0.0

def compute_area(a, b, c):
    """Return the area of the triangle with side lengths `a`, `b` and `c`.

    If the three lengths provided cannot form a triangle,
    then the area 0.0 is returned.

    """
    return 0.0
