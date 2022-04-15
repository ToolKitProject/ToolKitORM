from abc import ABC, abstractmethod
from typing import ClassVar

from toolkitorm import sql


class HasSQL(ABC):
    @abstractmethod
    def to_sql(self) -> str:
        pass


class HasName(ABC):
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
