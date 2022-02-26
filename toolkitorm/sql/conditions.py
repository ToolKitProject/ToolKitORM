from toolkitorm import SQL
from toolkitorm.sql.basistable import BasisTable
from toolkitorm.sql.dialect import BaseDialect


class Condition:
    table: type[BasisTable]
    left: SQL
    action: SQL
    right: SQL

    def __init__(
        self, table: type[BasisTable], left: SQL, action: SQL, right: SQL
    ) -> None:
        self.table = table
        self.left = left
        self.action = action
        self.right = right

    def __str__(self) -> str:
        return self.to_sql()

    def __and__(self, condition: "Condition") -> "Condition":
        return Condition(self.table, self.to_sql(), self.dialect.and_, condition.to_sql())

    def __or__(self, condition: "Condition") -> "Condition":
        return Condition(self.table, self.to_sql(), self.dialect.or_, condition.to_sql())

    @property
    def dialect(self) -> BaseDialect:
        return self.table.__dialect__

    def and_(self, *conditions: "Condition") -> "Condition":
        pass

    def or_(self, *conditions: "Condition") -> "Condition":
        pass

    def to_sql(self) -> SQL:
        return SQL(f"{self.left}{self.action}{self.right}")


__all__ = ["Condition"]
