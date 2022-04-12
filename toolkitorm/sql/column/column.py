from typing import Generic, Optional, overload

from toolkitorm import V, sql
from toolkitorm.sql.base import HasDialect, HasName
from toolkitorm.sql.condition import BaseCondition, Eq, Ge, Gt, In, Is, Le, Lt, Ne
from toolkitorm.sql.dialect import BaseDialect
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
    def __eq__(self, value: object) -> BaseCondition:  # type:ignore
        return Eq(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __ne__(self, value: object) -> BaseCondition:  # type:ignore
        return Ne(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __lt__(self, value: object) -> BaseCondition:
        return Lt(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __gt__(self, value: object) -> BaseCondition:
        return Gt(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __le__(self, value: object) -> BaseCondition:
        return Le(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def __ge__(self, value: object) -> BaseCondition:
        return Ge(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def IS(self, value: object) -> BaseCondition:
        return Is(self.__dialect__, self.sql_name, Data(self.value_type, value))

    def IN(self, *values: object) -> BaseCondition:
        return In(
            self.__dialect__,
            self.sql_name,
            [Data(self.value_type, v) for v in values],
        )


__all__ = [
    "BaseColumn",
]
