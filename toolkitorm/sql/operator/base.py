from abc import ABC

from toolkitorm import sql
from toolkitorm.sql.base import HasDialect, HasSQL
from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.storage import Data


class BaseOperator(HasSQL, HasDialect, ABC):
    def __init__(self, dialect: BaseDialect) -> None:
        self.__dialect__ = dialect

    def __str__(self) -> str:
        return self.to_sql()


class BaseCondition(BaseOperator, ABC):
    def __invert__(self) -> "sql.operator.Not":
        return sql.operator.Not(self.__dialect__, self)

    def __and__(self, other: "BaseCondition") -> "sql.operator.And":
        return sql.operator.And(self.__dialect__, self, other)

    def __or__(self, other: "BaseCondition") -> "sql.operator.Or":
        return sql.operator.Or(self.__dialect__, self, other)


class Math(BaseOperator, ABC):
    left: Data | str
    action: str
    right: Data

    def __init__(self, dialect: BaseDialect, l: Data | str, a: str, r: Data) -> None:
        super().__init__(dialect)
        self.left = l
        self.action = a
        self.right = r

    def to_sql(self) -> str:
        l = self.left.to_sql() if isinstance(self.left, Data) else self.left
        return f"{l} {self.action} {self.right.to_sql()}"


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


__all__ = [
    "BaseCondition",
    "Math",
    "Logical",
    "Comparison",
]
