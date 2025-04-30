# dummy-shape

Библиотека для работы с геометрическими фигурами на Python.  
Реализованы:

- **AbstractShape** — базовый класс (ABC) с метаклассом `ShapeMeta`, автоматически регистрирующим все подклассы фигур по имени.
- **Circle** — класс круг и метод `area()` для вычисления площади.
- **Triangle** — класс треугольник, метод `area()` для вычисления площади, метод `is_right()` для проверки является ли треугольник прямоугольным.
- __create_shape(name: str, *args, **kwargs)__ — функция фабрика, создающая фигуру по её имени (регистр нечувствителен).
- **UnknownShapeError** — исключение, если запрошено неизвестное (не зарегистрированное) имя фигуры.
- **InvalidValueError** — исключение для некорректных параметров фигур (например, отрицательное число).

---

## Установка для сторонних постащиков

```bash
pip install git+https://github.com/ralbakov/dummy_shape.git
```

## Установка для просмотра исходников и тестирования

1. Клонирование 
```bash
git clone https://github.com/ralbakov/dummy_shape.git
cd dummy-shape
```

2. Установка dev-зависимостей
```bash
poetry install --with dev
```

## Быстрый старт, описан в `main.py`

```python
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
```

## Тесты

1. Запустить pytest:
```bash
poetry run pytest -v
```


## API

`abstract_shape.py`

Базовый класс для всех фигур.

- `class AbstractShape(ABC, metaclass=ShapeMeta)`

___

`circle.py`
- `class Circle(AbstractShape)`
  - `Circle(radius: float)` — создаёт круг, если radius > 0, иначе InvalidValueError.
  - `area() -> float` — возвращает π × r².
  - `__str__() -> str` — Circle(radius=`<r>`).

___

`triangle.py`
- `class Triangle(AbstractShape)`
  - `Triangle(a: float, b: float, c: float)` — проверяет, что все стороны > 0 и удовлетворяют неравенствам треугольника, иначе InvalidValueError.
  - `area() -> float` — по формуле Герона.
  - `is_right() -> bool` — проверяет, прямоугольный ли треугольник.
  - `__str__() —> str` — Triangle(a=`<a>`, b=`<b>`, c=`<c>`).
___


## Добавление своих фигур

Чтобы зарегистрировать новую форму, достаточно определить подкласс AbstractShape в любом модуле вашего проекта:
```python
from dummy_shape import AbstractShape


class MyShape(AbstractShape):
    def __init__(self, *args):
        self.params = ...

    def area(self) -> float:
        return ...

    def __str__(self):
        return "MyShape(...)"
```

