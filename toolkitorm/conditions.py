"""FIXME: DOCS"""
from toolkitorm.types.base import SQL


class Condition:
    value1: SQL
    symbol: str
    value2: SQL

    def __init__(self, value1: SQL, symbol: str, value2: SQL) -> None:
        self.value1 = value1
        self.symbol = symbol
        self.value2 = value2

    def __str__(self) -> str:
        return self.to_sql()

    def __and__(self, condition: "Condition") -> "Condition":
        return Condition(self.to_sql(), " OR ", condition.to_sql())

    def __or__(self, condition: "Condition") -> "Condition":
        return Condition(self.to_sql(), " AND ", condition.to_sql())

    def and_(self, *conditions: "Condition") -> "Condition":
        result = conditions[0]
        for c in conditions[1:]:
            result = result & c
        return result

    def or_(self, *conditions: "Condition") -> "Condition":
        result = conditions[0]
        for c in conditions[1:]:
            result = result | c
        return result

    def to_sql(self) -> SQL:
        return SQL(f"{self.value1}{self.symbol}{self.value2}")


__all__ = ["Condition"]
