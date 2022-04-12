from typing import ClassVar
from toolkitorm import sql
from abc import ABC, abstractmethod


class HasSQL(ABC):
    @abstractmethod
    def to_sql(self) -> str:
        pass


class HasName:
    @property
    @abstractmethod
    def sql_name(self) -> str:
        pass


class HasDialect:
    __dialect__: "sql.dialect.BaseDialect"


__all__ = [
    "HasSQL",
    "HasName",
    "HasDialect",
]
