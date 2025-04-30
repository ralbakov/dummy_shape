import math

import pytest

from dummy_shape import create_shape, Circle, Triangle, UnknownShapeError


def test_create_circle():
    circle = create_shape("circle", 3)
    assert isinstance(circle, Circle)
    assert pytest.approx(circle.area()) == math.pi * 3**2


def test_create_triangle():
    triangle = create_shape("triangle", 6, 7, 8)
    assert isinstance(triangle, Triangle)
    assert triangle.area() > 0


def test_create_unknown_shape():
    with pytest.raises(UnknownShapeError):
        create_shape("hexagon", 1, 2, 3, 4, 5, 6)
