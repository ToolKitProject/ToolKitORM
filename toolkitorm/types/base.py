"""
FIXME: DOCS

TODO: Add exceptions
"""
from abc import ABC, abstractmethod
from ast import literal_eval
from datetime import date, datetime, time, timedelta
from decimal import Decimal as decimal
from json import dumps, loads
from typing import Generic, NewType, TypeVar

V = TypeVar("V")
SQL = NewType("SQL", str)

_T = TypeVar("_T")


class BaseType(Generic[V], ABC):
    """
    Abstract class for SQL data types
    """

    __type__: type[V]
    __type_name__: str
    __args__: tuple[object, ...]

    def __init__(self, *args: object) -> None:
        assert hasattr(self, "__type__")  # TODO
        assert hasattr(self, "__type_name__")  # TODO

        self.__args__ = args

    def __init_subclass__(cls, **kwargs: object) -> None:
        if not hasattr(cls, "__type_name__"):
            cls.__type_name__ = cls.__name__

    def to_sql(self, value: V | None) -> SQL:
        """
        Get python value and return 'repr SQL' value
        """
        if value is None:
            return SQL("NULL")
        else:
            return SQL(self._to(value))

    def from_sql(self, sql: SQL) -> V | None:
        """
        Get 'not repr SQL' value and return python value
        """
        if sql.upper() == "NULL":
            return None
        else:
            return self._from(sql)

    @property
    def sql_name(self) -> str:
        """Return name of the SQL type"""
        args = ",".join(map(str, self.__args__))
        return f"{self.__type_name__.upper()}({args})"

    @abstractmethod
    def _to(self, value: V) -> str:
        pass

    @abstractmethod
    def _from(self, sql: str) -> V:
        pass


class BaseAny(BaseType[object]):
    __type__ = object

    def _to(self, value: object) -> str:
        return repr(value)

    def _from(self, sql: str) -> object:
        return literal_eval(sql)


class BaseInteger(BaseType[int]):
    __type__ = int

    def _to(self, value: int) -> str:
        return repr(value)

    def _from(self, sql: str) -> int:
        return int(sql)


class BaseFloat(BaseType[float]):
    __type__ = float

    def _to(self, value: float) -> str:
        return repr(value)

    def _from(self, sql: str) -> float:
        return float(sql)


class BaseDecimal(BaseType[decimal]):
    __type__ = decimal

    def _to(self, value: decimal) -> str:
        return repr(str(value))

    def _from(self, sql: str) -> decimal:
        return decimal(sql)


class BaseString(BaseType[str]):
    __type__ = str

    def _to(self, value: str) -> str:
        return repr(value)

    def _from(self, sql: str) -> str:
        return sql


class BaseBool(BaseType[bool]):
    __type__ = bool

    def _to(self, value: bool) -> str:
        return str(value).upper()

    def _from(self, sql: str) -> bool:
        return True if sql.upper() in ("TRUE", "YES", "ON", "1") else False


class BaseList(BaseType[list[_T]]):
    __type__ = list

    def _to(self, value: list[_T]) -> str:
        return repr(dumps(value))

    def _from(self, sql: str) -> list[_T]:
        return loads(sql)


class BaseDict(BaseType[dict[str, _T]]):
    __type__ = dict

    def _to(self, value: dict[str, _T]) -> str:
        return repr(dumps(value))

    def _from(self, sql: str) -> dict[str, _T]:
        return loads(sql)


class BaseDate(BaseType[date]):
    __type__ = date

    def _to(self, value: date) -> str:
        return repr(value.isoformat())

    def _from(self, sql: str) -> date:
        return date.fromisoformat(sql)


class BaseTime(BaseType[time]):
    __type__ = time

    def _to(self, value: time) -> str:
        return repr(value.isoformat())

    def _from(self, sql: str) -> time:
        return time.fromisoformat(sql)


class BaseDatetime(BaseType[datetime]):
    __type__ = datetime

    def _to(self, value: datetime) -> str:
        return repr(value.isoformat())

    def _from(self, sql: str) -> datetime:
        return datetime.fromisoformat(sql)


class BaseTimedelta(BaseType[timedelta]):
    __type__ = timedelta

    def _to(self, value: timedelta) -> str:
        return repr(str(value.total_seconds()))

    def _from(self, sql: str) -> timedelta:
        return timedelta(seconds=float(sql))
