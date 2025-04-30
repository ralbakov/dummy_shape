import math

import pytest

from dummy_shape import Circle, InvalidValueError


def test_circle_area():
    radius = 2
    circle = Circle(radius)
    assert pytest.approx(circle.area(), rel=1e-9) == math.pi * radius**2

@pytest.mark.parametrize("r", [0, -1])
def test_circle_invalid_radius(r):
    with pytest.raises(InvalidValueError):
        Circle(r)
