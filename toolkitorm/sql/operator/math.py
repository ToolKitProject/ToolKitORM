from toolkitorm.sql.dialect.dialect import BaseDialect
from toolkitorm.sql.operator import Math
from toolkitorm.sql.storage.data import Data


class Add(Math):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.ADD, r)


class Sub(Math):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.SUB, r)


class Mul(Math):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.MUL, r)


class Div(Math):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.DIV, r)


class Mod(Math):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.MOD, r)


__all__ = [
    "Add",
    "Sub",
    "Mul",
    "Div",
    "Mod",
]
