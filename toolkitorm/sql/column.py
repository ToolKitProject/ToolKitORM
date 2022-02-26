from typing import Generic, Optional, overload

from toolkitorm.sql.dialect import BaseDialect

from .basistable import BasisTable
from .conditions import Condition
from .storage import Data
from .types import BaseType
from toolkitorm import V, SQL


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
    def __get__(self, instance: None, owner: type[BasisTable]) -> "BaseColumn":
        ...

    def __get__(
        self,
        instance: BasisTable | None,
        owner: type[BasisTable],
    ) -> V | "BaseColumn" | None:
        if instance is None:
            return self
        return self.data(instance).to_python()

    def data(self, instance: BasisTable) -> Data[V]:
        return instance.__storage__.get(self.name)

    @property
    def sql_name(self) -> SQL:
        return self.__dialect__.struct(SQL(self.name))

    #! This violates the Liskov substitution principle
    def __eq__(self, value: V) -> Condition:  # type:ignore
        return Condition(
            self.table, self.sql_name, self.__dialect__.eq, self.value_type.to_sql(value)
        )

    def __ne__(self, value: V) -> Condition:  # type:ignore
        return Condition(
            self.table, self.sql_name, self.__dialect__.ne, self.value_type.to_sql(value)
        )

    def __lt__(self, value: V) -> Condition:
        return Condition(
            self.table, self.sql_name, self.__dialect__.lt, self.value_type.to_sql(value)
        )

    def __gt__(self, value: V) -> Condition:
        return Condition(
            self.table, self.sql_name, self.__dialect__.gt, self.value_type.to_sql(value)
        )

    def __le__(self, value: V) -> Condition:
        return Condition(
            self.table, self.sql_name, self.__dialect__.le, self.value_type.to_sql(value)
        )

    def __ge__(self, value: V) -> Condition:
        return Condition(
            self.table, self.sql_name, self.__dialect__.ge, self.value_type.to_sql(value)
        )


__all__ = ["BaseColumn"]
