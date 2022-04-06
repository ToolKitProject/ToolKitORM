from abc import ABC, abstractmethod

from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.storage import Data


class BaseCondition(ABC):
    __dialect__: BaseDialect

    def __init__(self, dialect: BaseDialect) -> None:
        self.__dialect__ = dialect

    def __str__(self) -> str:
        return self.to_sql()

    def __invert__(self) -> "Not":
        return Not(self.__dialect__, self)

    def __and__(self, other: "BaseCondition") -> "And":
        return And(self.__dialect__, self, other)

    def __or__(self, other: "BaseCondition") -> "Or":
        return Or(self.__dialect__, self, other)

    @abstractmethod
    def to_sql(self) -> str:
        pass


class Logical(BaseCondition):
    left: BaseCondition
    action: str
    right: BaseCondition

    def __init__(
        self, dialect: BaseDialect, l: BaseCondition, a: str, r: BaseCondition
    ) -> None:
        super().__init__(dialect)
        self.left = l
        self.action = a
        self.right = r

    def to_sql(self) -> str:
        return f"({self.left.to_sql()}) {self.action} ({self.right.to_sql()})"


class Comparison(BaseCondition):
    left: str
    action: str
    right: Data

    def __init__(self, dialect: BaseDialect, l: str, a: str, r: Data) -> None:
        super().__init__(dialect)
        self.left = l
        self.action = a
        self.right = r

    def to_sql(self) -> str:
        return f"{self.left} {self.action} {self.right.to_sql()}"


class Not(BaseCondition):
    condition: BaseCondition

    def __init__(self, dialect: BaseDialect, c: BaseCondition) -> None:
        super().__init__(dialect)
        self.condition = c

    def to_sql(self) -> str:
        return f"{self.__dialect__.NOT} ({self.condition.to_sql()})"


class And(Logical):
    def __init__(self, dialect: BaseDialect, l: BaseCondition, r: BaseCondition) -> None:
        super().__init__(dialect, l, dialect.AND, r)


class Or(Logical):
    def __init__(self, dialect: BaseDialect, l: BaseCondition, r: BaseCondition) -> None:
        super().__init__(dialect, l, dialect.OR, r)


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
        return f"{self.left} {self.__dialect__.IN} ({','.join([d.to_sql() for d in self.right])})"


def not_(c: BaseCondition) -> Not:
    return ~c


def and_(l: BaseCondition, r: BaseCondition) -> And:
    return l & r


def or_(l: BaseCondition, r: BaseCondition) -> Or:
    return l | r


__all__ = [
    "BaseCondition",
    "not_",
    "and_",
    "or_",
    "Not",
    "And",
    "Or",
    "Eq",
    "Ne",
    "Gt",
    "Lt",
    "Ge",
    "Le",
    "Is",
    "In",
]
