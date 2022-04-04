from abc import ABC, abstractmethod


class Condition(ABC):
    def __str__(self) -> str:
        return self.to_sql()

    def __invert__(self) -> "Not":
        return Not(self)

    def __and__(self, other: "Condition") -> "And":
        return And(self, other)

    def __or__(self, other: "Condition") -> "Or":
        return Or(self, other)

    @abstractmethod
    def to_sql(self) -> str:
        pass


class Comparison(Condition):
    left: str
    action: str
    right: str

    def __init__(self, l: str, action: str, r: str) -> None:
        super().__init__()
        self.left = l
        self.action = action
        self.right = r

    def to_sql(self) -> str:
        return f"{self.left} {self.action} {self.right}"


class Logical(Condition):
    left: Condition
    action: str
    right: Condition

    def __init__(self, l: Condition, action: str, r: Condition) -> None:
        super().__init__()
        self.left = l
        self.action = action
        self.right = r

    def to_sql(self) -> str:
        return f"{self.left.to_sql()} {self.action} {self.right.to_sql()}"


class Not(Condition):
    condition: Condition

    def __init__(self, c: Condition) -> None:
        super().__init__()
        self.condition = c

    def to_sql(self) -> str:
        return f"NOT ({self.condition.to_sql()})"


class And(Logical):
    def __init__(self, l: Condition, r: Condition) -> None:
        super().__init__(l, "AND", r)


class Or(Logical):
    def __init__(self, l: Condition, r: Condition) -> None:
        super().__init__(l, "OR", r)


class Is(Comparison):
    def __init__(self, l: str, r: str) -> None:
        super().__init__(l, "IS", r)


class In(Comparison):
    def __init__(self, l: str, r: list[str]) -> None:
        super().__init__(l, "IN", f"({','.join(r)})")


class Eq(Comparison):
    def __init__(self, l: str, r: str) -> None:
        super().__init__(l, "=", r)


class Ne(Comparison):
    def __init__(self, l: str, r: str) -> None:
        super().__init__(l, "!=", r)


class Gt(Comparison):
    def __init__(self, l: str, r: str) -> None:
        super().__init__(l, ">", r)


class Lt(Comparison):
    def __init__(self, l: str, r: str) -> None:
        super().__init__(l, "<", r)


class Ge(Comparison):
    def __init__(self, l: str, r: str) -> None:
        super().__init__(l, ">=", r)


class Le(Comparison):
    def __init__(self, l: str, r: str) -> None:
        super().__init__(l, "<=", r)


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
]
