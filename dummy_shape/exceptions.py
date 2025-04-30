class ShapeError(Exception):
    pass


class InvalidValueError(ShapeError):
    pass


class UnknownShapeError(ShapeError):
    def __init__(self, name: str) -> None:
        super().__init__(f"Shape '{name}' not recognised")
