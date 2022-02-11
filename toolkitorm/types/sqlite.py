"""FIXME: DOCS"""
from toolkitorm.types.base import (
    _T,
    BaseAny,
    BaseBool,
    BaseDate,
    BaseDatetime,
    BaseDecimal,
    BaseDict,
    BaseFloat,
    BaseInteger,
    BaseList,
    BaseString,
    BaseTime,
    BaseTimedelta,
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


__all__ = [
    "Integer",
    "Real",
    "Text",
    "Blob",
    "Boolean",
    "Decimal",
    "Time",
    "Date",
    "Datetime",
    "Timedelta",
    "Dict",
    "List",
]
