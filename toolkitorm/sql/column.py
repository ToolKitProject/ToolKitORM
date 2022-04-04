from typing import Generic, Optional, overload

from toolkitorm import V
from toolkitorm.sql.basistable import BasisTable
from toolkitorm.sql.conditions import Condition, Eq, Ge, Gt, In, Is, Le, Lt, Ne
from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.storage import Data
from toolkitorm.sql.types import BaseType


class BaseColumn(Generic[V]):
    """Column without dialect"""

    __dialect__: BaseDialect

    table: type[BasisTable]
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

    def __set_name__(self, owner: type[BasisTable], name: str) -> None:
        self.table = owner
        self.name = name

    @overload
    def __get__(self, instance: BasisTable, owner: type[BasisTable]) -> V | None:
        ...

    @overload
    def __get__(self, instance: None, owner: type[BasisTable]) -> "BaseColumn[V]":
        ...

    def __get__(
        self, instance: BasisTable | None, owner: type[BasisTable]
    ) -> V | "BaseColumn[V]" | None:
        if instance is None:
            return self
        return self.data(instance).to_python()

    def data(self, instance: BasisTable) -> Data[V]:
        return instance.__storage__.get(self.name)

    @property
    def sql_name(self) -> str:
        return f"{self.table.sql_name}.{self.__dialect__.name(self.name)}"

    #! This violates the Liskov substitution principle
    def __eq__(self, value: object) -> Condition:  # type:ignore
        return Eq(self.__dialect__, self.sql_name, self.value_type.to_sql(value))

    def __ne__(self, value: object) -> Condition:  # type:ignore
        return Ne(self.__dialect__, self.sql_name, self.value_type.to_sql(value))

    def __lt__(self, value: object) -> Condition:
        return Lt(self.__dialect__, self.sql_name, self.value_type.to_sql(value))

    def __gt__(self, value: object) -> Condition:
        return Gt(self.__dialect__, self.sql_name, self.value_type.to_sql(value))

    def __le__(self, value: object) -> Condition:
        return Le(self.__dialect__, self.sql_name, self.value_type.to_sql(value))

    def __ge__(self, value: object) -> Condition:
        return Ge(self.__dialect__, self.sql_name, self.value_type.to_sql(value))

    def IS(self, value: object) -> Condition:
        return Is(self.__dialect__, self.sql_name, self.value_type.to_sql(value))

    def IN(self, *values: object) -> Condition:
        return In(
            self.__dialect__,
            self.sql_name,
            [self.value_type.to_sql(v) for v in values],
        )


__all__ = ["BaseColumn"]
