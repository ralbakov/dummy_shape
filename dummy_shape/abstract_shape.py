from abc import ABC, abstractmethod, ABCMeta


class ShapeMeta(ABCMeta):
    SHAPE_NAME_TO_SHAPE_TYPE: dict[str, type] = {}

    def __init__(cls, name, bases, namespace) -> None:
        super().__init__(name, bases, namespace)
        if not getattr(cls, "__abstractmethods__", False):
            ShapeMeta.SHAPE_NAME_TO_SHAPE_TYPE[name.lower()] = cls


class AbstractShape(ABC, metaclass=ShapeMeta):
    @abstractmethod
    def area(self) -> float:
        pass
