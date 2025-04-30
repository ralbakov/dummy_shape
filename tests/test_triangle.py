import pytest

from dummy_shape import Triangle, InvalidValueError


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert pytest.approx(triangle.area(), rel=1e-9) == 6.0


def test_triangle_invalid_sides():
    with pytest.raises(InvalidValueError):
        Triangle(1, 2, 3)


def test_triangle_is_right_true():
    triangle = Triangle(5, 3, 4)
    assert triangle.is_right() is True


def test_triangle_is_right_false():
    triangle = Triangle(2, 3, 4)
    assert triangle.is_right() is False


@pytest.mark.parametrize("sides", [(1,2,3), (0,1,1), (-1,2,2)])
def test_triangle_invalid(sides):
    with pytest.raises(InvalidValueError):
        Triangle(*sides)
