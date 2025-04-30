import math

from .abstract_shape import AbstractShape
from .exceptions import InvalidValueError


class Circle(AbstractShape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise InvalidValueError(f"Radius must be positive. Now {radius} <= 0")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"
