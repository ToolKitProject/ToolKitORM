from abc import ABC

from toolkitorm import sql
from toolkitorm.sql.base import HasDialect, HasSQL
from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.storage import Data


class BaseCondition(HasSQL, HasDialect, ABC):
    def __init__(self, dialect: BaseDialect) -> None:
        self.__dialect__ = dialect

    def __str__(self) -> str:
        return self.to_sql()

    def __invert__(self) -> "sql.condition.Not":
        return sql.condition.Not(self.__dialect__, self)

    def __and__(self, other: "BaseCondition") -> "sql.condition.And":
        return sql.condition.And(self.__dialect__, self, other)

    def __or__(self, other: "BaseCondition") -> "sql.condition.Or":
        return sql.condition.Or(self.__dialect__, self, other)


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
    "Logical",
    "Comparison",
]
