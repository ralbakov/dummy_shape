from dummy_shape import create_shape, UnknownShapeError, AbstractShape, InvalidValueError

# Добавление новой фигуры
class Rectangle(AbstractShape):
    def __init__(self, width: int, height: int) -> None:
        if width <= 0 or height <= 0:
            raise InvalidValueError(f"width or height must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"This is a newly added shape. Rectangle(width={self.width}, height={self.height})"


if __name__ == "__main__":
    circle = create_shape("circle", 5)
    print(f'{circle}, s = {circle.area()}', end='\n\n')

    triangle = create_shape("triangle", 3, 4, 5)
    print(f'{triangle}, s = {triangle.area()}, right triangle = {triangle.is_right()}', end='\n\n')

    try:
        hexagon = create_shape("hexagon", 1, 2, 3, 4, 5, 6)
    except UnknownShapeError as e:
        print(repr(e), end='\n\n')

    rectangle = create_shape("rectangle", 5, 3)
    print(f'{rectangle}, s = {rectangle.area()}')
