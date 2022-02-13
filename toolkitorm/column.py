"""FIXME: DOCS"""
from typing import Generic, Optional

from toolkitorm.basetable import BaseTable
from toolkitorm.conditions import Condition
from toolkitorm.storage import Data
from toolkitorm.types.base import SQL, BaseType, V


class Column(Generic[V]):
    table: type[BaseTable]
    name: str
    value_type: BaseType[V]
    default: V | None
    nullable: bool
    auto: bool
    unique: bool
    primary: bool
    foreign: Optional["Column[V]"]

    def __init__(
        self,
        value_type: BaseType[V],
        default: V | None = None,
        nullable: bool = False,
        auto: bool = False,
        unique: bool = False,
        primary: bool = False,
        foreign: Optional["Column[V]"] = None,
    ) -> None:
        self.value_type = value_type
        self.default = default
        self.nullable = nullable
        self.auto = auto
        self.unique = unique
        self.primary = primary
        self.foreign = foreign

        if self.auto:
            self.nullable = True
        if self.primary:
            self.nullable = True
            self.unique = True

    def __set_name__(self, owner: type[BaseTable], name: str) -> None:
        self.table = owner
        self.name = name

    def __get__(self, instance: BaseTable, owner: type[BaseTable]) -> V | None:
        return self.data(instance).to_python()

    def data(self, instance: BaseTable) -> Data[V]:
        return instance.__storage__.get(self.name)

    @property
    def sql_name(self) -> SQL:
        return SQL(f"{self.name}")

    #! This violates the Liskov substitution principle
    def __eq__(self, value: V) -> Condition:  # type:ignore
        return Condition(self.sql_name, "=", self.value_type.to_sql(value))

    def __ne__(self, value: V) -> Condition:  # type:ignore
        return Condition(self.sql_name, "!=", self.value_type.to_sql(value))

    def __lt__(self, value: V) -> Condition:
        return Condition(self.sql_name, "<", self.value_type.to_sql(value))

    def __gt__(self, value: V) -> Condition:
        return Condition(self.sql_name, ">", self.value_type.to_sql(value))

    def __le__(self, value: V) -> Condition:
        return Condition(self.sql_name, "<=", self.value_type.to_sql(value))

    def __ge__(self, value: V) -> Condition:
        return Condition(self.sql_name, ">=", self.value_type.to_sql(value))


__all__ = ["Column"]
