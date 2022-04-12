from typing import Generic, Optional, overload

from toolkitorm import V, sql
from toolkitorm.sql.base import HasDialect, HasName
from toolkitorm.sql.operator import (
    Add,
    Div,
    Eq,
    Ge,
    Gt,
    In,
    Is,
    Le,
    Lt,
    Mod,
    Mul,
    Ne,
    Sub,
)
from toolkitorm.sql.storage import Data
from toolkitorm.sql.types import BaseType


class BaseColumn(HasName, HasDialect, Generic[V]):
    table: type["sql.table.BaseTable"]
    name: str
    value_type: BaseType[V]
    default: V | None
    nullable: bool
    auto: bool
    unique: bool
    primary: bool
    foreign: Optional["BaseColumn[V]"]

    def __init__(
        self,
        value_type: BaseType[V],
        default: V | None = None,
        nullable: bool = False,
        auto: bool = False,
        unique: bool = False,
        primary: bool = False,
        foreign: Optional["BaseColumn[V]"] = None,
    ) -> None:
        assert type(value_type.__dialect__) is type(self.__dialect__)
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

    def __set_name__(self, owner: type["sql.table.BaseTable"], name: str) -> None:
        self.table = owner
        self.name = name

    @overload
    def __get__(
        self, instance: "sql.table.BaseTable", owner: type["sql.table.BaseTable"]
    ) -> V | None:
        ...

    @overload
    def __get__(
        self, instance: None, owner: type["sql.table.BaseTable"]
    ) -> "BaseColumn[V]":
        ...

    def __get__(
        self,
        instance: Optional["sql.table.BaseTable"],
        owner: type["sql.table.BaseTable"],
    ) -> V | "BaseColumn[V]" | None:
        if instance is None:
            return self
        return self.data(instance).get()

    def data(self, instance: "sql.table.BaseTable") -> Data[V]:
        return instance.__storage__.get(self.name)

    @property
    def sql_name(self) -> str:
        return f"{self.table.sql_name}.{self.__dialect__.name(self.name)}"

    #! This violates the Liskov substitution principle
    def __add__(self, value: object) -> Add:  # type:ignore
        return Add(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __sub__(self, value: object) -> Sub:  # type:ignore
        return Sub(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __mul__(self, value: object) -> Mul:  # type:ignore
        return Mul(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __truediv__(self, value: object) -> Div:  # type:ignore
        return Div(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __mod__(self, value: object) -> Mod:  # type:ignore
        return Mod(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __eq__(self, value: object) -> Eq:  # type:ignore
        return Eq(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __ne__(self, value: object) -> Ne:  # type:ignore
        return Ne(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __lt__(self, value: object) -> Lt:
        return Lt(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __gt__(self, value: object) -> Gt:
        return Gt(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __le__(self, value: object) -> Le:
        return Le(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __ge__(self, value: object) -> Ge:
        return Ge(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def IS(self, value: object) -> Is:
        return Is(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def IN(self, *values: object) -> In:
        return In(
            self.__dialect__,
            self.sql_name,
            [Data(self.value_type, v) for v in values],
        )


__all__ = [
    "BaseColumn",
]
