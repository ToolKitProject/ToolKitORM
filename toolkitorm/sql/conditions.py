from toolkitorm.sql.basistable import BasisTable
from toolkitorm.sql.dialect import BaseDialect


class Condition:
    table: type[BasisTable]
    left: str
    action: str
    right: str

    def __init__(
        self, table: type[BasisTable], left: str, action: str, right: str
    ) -> None:
        self.table = table
        self.left = left
        self.action = action
        self.right = right

    def __str__(self) -> str:
        return self.to_sql()

    def __and__(self, condition: "Condition") -> "Condition":
        return Condition(self.table, self.to_sql(), self.dialect.AND, condition.to_sql())

    def __or__(self, condition: "Condition") -> "Condition":
        return Condition(self.table, self.to_sql(), self.dialect.OR, condition.to_sql())

    @property
    def dialect(self) -> BaseDialect:
        return self.table.__dialect__

    def to_sql(self) -> str:
        return f"{self.left} {self.action} {self.right}"

    def AND(self, condition: "Condition") -> "Condition":
        return self & condition

    def OR(self, condition: "Condition") -> "Condition":
        return self | condition

    def NOT(self) -> "Condition":  # Cry about it FIXME
        return Condition(self.table, self.dialect.NOT, f"( {self.to_sql()}", ")")


__all__ = ["Condition"]
