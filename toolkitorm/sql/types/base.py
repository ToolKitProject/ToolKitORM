from abc import ABC, abstractmethod
from typing import Generic

from toolkitorm import V
from toolkitorm.sql.base import HasDialect, HasSQL


class BaseType(HasSQL, HasDialect, Generic[V], ABC):
    __type__: type[V]
    __type_name__: str
    __args__: tuple[object, ...]

    def __init__(self, *args: object) -> None:
        assert hasattr(self, "__type__")  # TODO
        if not hasattr(self, "__type_name__"):
            self.__type_name__ = type(self).__name__
        assert hasattr(self, "__dialect__")  # TODO
        self.__args__ = args

    def convert_to_sql(self, value: V | None) -> str:
        if value is None:
            return self.__dialect__.NULL
        else:
            return self._to(value)

    def convert_from_sql(self, value: object) -> V | None:
        if isinstance(value, self.__type__) or value is None:
            return value
        elif str(value).upper() == self.__dialect__.NULL:
            return None
        else:
            return self._from(str(value))

    def to_sql(self) -> str:
        return (
            f'{self.__type_name__.upper()}({",".join([str(a) for a in self.__args__])})'
        )

    @abstractmethod
    def _to(self, value: V) -> str:
        pass

    @abstractmethod
    def _from(self, sql: str) -> V:
        pass


__all__ = [
    "BaseType",
]
