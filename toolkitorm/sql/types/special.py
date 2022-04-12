from datetime import date, datetime, time, timedelta
from decimal import Decimal as decimal
from json import dumps, loads

from toolkitorm import V
from toolkitorm.sql.types import BaseType


class BaseDecimal(BaseType[decimal]):
    __type__ = decimal

    def _to(self, value: decimal) -> str:
        return str(value)

    def _from(self, sql: str) -> decimal:
        return decimal(sql)


class BaseList(BaseType[list[V]]):
    __type__ = list

    def _to(self, value: list[V]) -> str:
        return self.__dialect__.string(dumps(value))

    def _from(self, sql: str) -> list[V]:
        return loads(sql)


class BaseDict(BaseType[dict[str, V]]):
    __type__ = dict

    def _to(self, value: dict[str, V]) -> str:
        return self.__dialect__.string(dumps(value))

    def _from(self, sql: str) -> dict[str, V]:
        return loads(sql)


class BaseDate(BaseType[date]):
    __type__ = date

    def _to(self, value: date) -> str:
        return self.__dialect__.string(value.isoformat())

    def _from(self, sql: str) -> date:
        return date.fromisoformat(sql)


class BaseTime(BaseType[time]):
    __type__ = time

    def _to(self, value: time) -> str:
        return self.__dialect__.string(value.isoformat())

    def _from(self, sql: str) -> time:
        return time.fromisoformat(sql)


class BaseDatetime(BaseType[datetime]):
    __type__ = datetime

    def _to(self, value: datetime) -> str:
        return self.__dialect__.string(value.isoformat(" "))

    def _from(self, sql: str) -> datetime:
        return datetime.fromisoformat(sql)


class BaseTimedelta(BaseType[timedelta]):
    __type__ = timedelta

    def _to(self, value: timedelta) -> str:
        return self.__dialect__.string(str(value.total_seconds()))

    def _from(self, sql: str) -> timedelta:
        return timedelta(seconds=float(sql))


__all__ = [
    "BaseDecimal",
    "BaseList",
    "BaseDict",
    "BaseDate",
    "BaseTime",
    "BaseDatetime",
    "BaseTimedelta",
]
