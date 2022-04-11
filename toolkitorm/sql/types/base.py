from abc import ABC, abstractmethod
from typing import Generic

from toolkitorm import V
from toolkitorm.sql.dialect import BaseDialect


class BaseType(Generic[V], ABC):
    """Abstract class for SQL data types"""

    __type__: type[V]
    __type_name__: str
    __dialect__: BaseDialect
    __args__: tuple[object, ...]

    def __init__(self, *args: object) -> None:
        assert hasattr(self, "__type__")  # TODO
        if not hasattr(self, "__type_name__"):
            self.__type_name__ = type(self).__name__
        assert hasattr(self, "__dialect__")  # TODO
        self.__args__ = args

    def convert(self, value: object) -> V | None:
        """
        Get any value and return python value (Implicit conversion)
        """
        if isinstance(value, self.__type__) or value is None:
            return value
        else:
            return self.from_sql(str(value))

    def to_sql(self, value: object) -> str:
        """
        Get python value and return 'repr SQL' value
        """
        v = self.convert(value)
        if v is None:
            return self.__dialect__.NULL
        else:
            return self._to(v)

    def from_sql(self, sql: str) -> V | None:
        """
        Get 'not repr SQL' value and return python value
        """
        if sql.upper() == self.__dialect__.NULL:
            return None
        else:
            return self._from(sql)

    @property
    def sql_name(self) -> str:
        """Return name of the SQL type"""
        args = ",".join([str(a) for a in self.__args__])
        return f"{self.__type_name__.upper()}({args})"

    @abstractmethod
    def _to(self, value: V) -> str:
        pass

    @abstractmethod
    def _from(self, sql: str) -> V:
        pass


__all__ = ["BaseType"]
