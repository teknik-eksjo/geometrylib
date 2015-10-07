"""Routines to test triangle properties without explicit instantiation."""

from geometrylib.shape import Triangle

def _make_triangle(a, b, c):
    try:
        return Triangle(a, b, c)
    except ValueError:
        return None

def is_triangle(a, b, c):
    """Test whether lengths `a`, `b` and `c` can be the sides of a triangle."""
    triangle = _make_triangle(a, b, c)
    return not triangle is None

def is_equilateral(a, b, c):
    """Return whether lengths `a`, `b` and `c` are an equilateral triangle."""
    triangle = _make_triangle(a, b, c)
    if triangle is None:
        return False
    return triangle.is_equilateral()

def is_isosceles(a, b, c):
    """Return whether lengths `a`, `b` and `c` are an isosceles triangle."""
    triangle = _make_triangle(a, b, c)
    if triangle is None:
        return False
    return triangle.is_isosceles()

def compute_perimiter(a, b, c):
    """Return the perimeter of the triangle with side lengths `a`, `b` and `c`.

    If the three lengths provided cannot form a triangle,
    then the perimeter 0 is returned.

    """
    triangle = _make_triangle(a, b, c)
    if triangle is None:
        return 0
    return triangle.perimeter()

def compute_area(a, b, c):
    """Return the area of the triangle with side lengths `a`, `b` and `c`.

    If the three lengths provided cannot form a triangle,
    then the area 0 is returned.

    """
    triangle = _make_triangle(a, b, c)
    if triangle is None:
        return 0
    return triangle.area()
