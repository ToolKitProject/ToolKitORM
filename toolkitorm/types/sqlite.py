"""FIXME: DOCS"""
from toolkitorm.types.base import (
    BaseAny,
    BaseInteger,
    BaseFloat,
    BaseDecimal,
    BaseString,
    BaseBool,
    BaseList,
    BaseDict,
    BaseDate,
    BaseTime,
    BaseDatetime,
    BaseTimedelta,
    _T,
)


# Built-in types
class Integer(BaseInteger):
    pass


class Real(BaseFloat):
    pass


class Text(BaseString):
    pass


class Blob(BaseAny):
    pass


# ORM types
class Boolean(BaseBool):
    __type_name__ = Integer.__type_name__

    def _from(self, sql: str) -> bool:
        return bool(int(sql))


class Decimal(BaseDecimal):
    __type_name__ = Text.__type_name__


class Time(BaseTime):
    __type_name__ = Text.__type_name__


class Date(BaseDate):
    __type_name__ = Text.__type_name__


class Datetime(BaseDatetime):
    __type_name__ = Text.__type_name__


class Timedelta(BaseTimedelta):
    __type_name__ = Text.__type_name__


class Dict(BaseDict[_T]):
    __type_name__ = Text.__type_name__


class List(BaseList[_T]):
    __type_name__ = Text.__type_name__
