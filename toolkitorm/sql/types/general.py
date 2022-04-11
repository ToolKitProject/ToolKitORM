from ast import literal_eval

from toolkitorm.sql.types import BaseType


class BaseAny(BaseType[object]):
    __type__ = object

    def _to(self, value: object) -> str:
        return self.__dialect__.string(value)

    def _from(self, sql: str) -> object:
        return literal_eval(sql)


class BaseInteger(BaseType[int]):
    __type__ = int

    def _to(self, value: int) -> str:
        return str(value)

    def _from(self, sql: str) -> int:
        return int(sql)


class BaseFloat(BaseType[float]):
    __type__ = float

    def _to(self, value: float) -> str:
        return str(value)

    def _from(self, sql: str) -> float:
        return float(sql)


class BaseString(BaseType[str]):
    __type__ = str

    def _to(self, value: str) -> str:
        return self.__dialect__.string(value)

    def _from(self, sql: str) -> str:
        return sql


class BaseBool(BaseType[bool]):
    __type__ = bool

    def _to(self, value: bool) -> str:
        return self.__dialect__.TRUE[0] if value else self.__dialect__.FALSE[0]

    def _from(self, sql: str) -> bool:
        return True if sql.upper() in self.__dialect__.TRUE else False


__all__ = [
    "BaseAny",
    "BaseInteger",
    "BaseFloat",
    "BaseString",
    "BaseBool",
]
