import math

from .abstract_shape import AbstractShape
from .exceptions import InvalidValueError


class Triangle(AbstractShape):
    def __init__(self, a: float, b: float, c: float) -> None:
        sides = sorted((a, b, c))
        if any(side <= 0 for side in sides) or sides[0] + sides[1] <= sides[2]:
            raise InvalidValueError("Sides cannot form a triangle")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        return math.isclose(self.a**2 + self.b**2, self.c**2, rel_tol=1e-9)

    def __str__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
