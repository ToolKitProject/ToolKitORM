from toolkitorm.sql.condition import Comparison
from toolkitorm.sql.condition.base import BaseCondition
from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.storage import Data


class Eq(Comparison):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.EQ, r)


class Ne(Comparison):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.NE, r)


class Gt(Comparison):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.GT, r)


class Lt(Comparison):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.LT, r)


class Ge(Comparison):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.GE, r)


class Le(Comparison):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.LE, r)


class Is(Comparison):
    def __init__(self, dialect: BaseDialect, l: str, r: Data) -> None:
        super().__init__(dialect, l, dialect.IS, r)


class In(BaseCondition):
    left: str
    action: str
    right: list[Data]

    def __init__(self, dialect: BaseDialect, l: str, r: list[Data]) -> None:
        super().__init__(dialect)
        self.left = l
        self.action = dialect.IN
        self.right = r

    def to_sql(self) -> str:
        return f"{self.left} {self.action} ({','.join([d.to_sql() for d in self.right])})"


__all__ = [
    "Eq",
    "Ne",
    "Gt",
    "Lt",
    "Ge",
    "Le",
    "Is",
    "In",
]
