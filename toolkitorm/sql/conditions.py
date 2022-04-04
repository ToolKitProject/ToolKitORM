from abc import ABC, abstractmethod

from toolkitorm.sql.dialect import BaseDialect


class Condition(ABC):
    __dialect__: BaseDialect

    def __init__(self, dialect: BaseDialect) -> None:
        self.__dialect__ = dialect

    def __str__(self) -> str:
        return self.to_sql()

    def __invert__(self) -> "Not":
        return Not(self.__dialect__, self)

    def __and__(self, other: "Condition") -> "And":
        return And(self.__dialect__, self, other)

    def __or__(self, other: "Condition") -> "Or":
        return Or(self.__dialect__, self, other)

    @abstractmethod
    def to_sql(self) -> str:
        pass


class Logical(Condition):
    left: Condition
    action: str
    right: Condition

    def __init__(self, dialect: BaseDialect, l: Condition, a: str, r: Condition) -> None:
        super().__init__(dialect)
        self.left = l
        self.action = a
        self.right = r

    def to_sql(self) -> str:
        return f"{self.left.to_sql()} {self.action} {self.right.to_sql()}"


class Compression(Condition):
    left: str
    action: str
    right: str

    def __init__(self, dialect: BaseDialect, l: str, a: str, r: str) -> None:
        super().__init__(dialect)
        self.left = l
        self.action = a
        self.right = r

    def to_sql(self) -> str:
        return f"{self.left} {self.action} {self.right}"


class Not(Condition):
    condition: Condition

    def __init__(self, dialect: BaseDialect, c: Condition) -> None:
        super().__init__(dialect)
        self.condition = c

    def to_sql(self) -> str:
        return f"{self.__dialect__.NOT} ({self.condition.to_sql()})"


class And(Logical):
    def __init__(self, dialect: BaseDialect, l: Condition, r: Condition) -> None:
        super().__init__(dialect, l, dialect.AND, r)


class Or(Logical):
    def __init__(self, dialect: BaseDialect, l: Condition, r: Condition) -> None:
        super().__init__(dialect, l, dialect.OR, r)


class Eq(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: str) -> None:
        super().__init__(dialect, l, dialect.EQ, r)


class Ne(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: str) -> None:
        super().__init__(dialect, l, dialect.EQ, r)


class Gt(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: str) -> None:
        super().__init__(dialect, l, dialect.GT, r)


class Lt(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: str) -> None:
        super().__init__(dialect, l, dialect.LT, r)


class Ge(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: str) -> None:
        super().__init__(dialect, l, dialect.GE, r)


class Le(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: str) -> None:
        super().__init__(dialect, l, dialect.LE, r)


class Is(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: str) -> None:
        super().__init__(dialect, l, dialect.IS, r)


class In(Compression):
    def __init__(self, dialect: BaseDialect, l: str, r: list[str]) -> None:
        super().__init__(dialect, l, dialect.IN, f"({','.join(r)})")


def not_(c: Condition) -> Not:
    return ~c


def and_(l: Condition, r: Condition) -> And:
    return l & r


def or_(l: Condition, r: Condition) -> Or:
    return l | r


__all__ = [
    "Condition",
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
