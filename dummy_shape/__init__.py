from .abstract_shape import ShapeMeta, AbstractShape
from .circle import Circle
from .exceptions import InvalidValueError, UnknownShapeError
from .triangle import Triangle


__all__ = [AbstractShape, Circle, InvalidValueError, UnknownShapeError, Triangle, 'create_shape']


def create_shape(name: str, *args, **kwargs) -> AbstractShape:
    try:
        shape_type = ShapeMeta.SHAPE_NAME_TO_SHAPE_TYPE[name.lower()]
    except KeyError:
        raise UnknownShapeError(name)
    return shape_type(*args, **kwargs)
