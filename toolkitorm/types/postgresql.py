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
class Smallint(BaseInteger):
    pass


class Integer(BaseInteger):
    pass


class Bigint(BaseInteger):
    pass


class Decimal(BaseDecimal):
    def __init__(self, precision: int, scale: int) -> None:
        super().__init__(precision, scale)


class Real(BaseFloat):
    pass


class Double(BaseFloat):
    __type_name__ = "double precision"


class Varchar(BaseString):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Char(BaseString):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Text(BaseString):
    pass


class Timestamp(BaseDatetime):
    pass


class TimestampTZ(BaseDatetime):
    pass


class Date(BaseDate):
    pass


class Time(BaseTime):
    pass


class TimeTZ(BaseTime):
    pass


class Interval(BaseTimedelta):
    pass


class Boolean(BaseBool):
    pass


class JSON(BaseDict[_T]):
    pass


class JSONB(BaseDict[_T]):
    pass


# ORM types
class Dynamic(BaseAny):
    __type_name__ = Text.__type_name__


class List(BaseList[_T]):
    __type_name__ = Text.__type_name__


__all__ = [
    "Smallint",
    "Integer",
    "Bigint",
    "Decimal",
    "Real",
    "Double",
    "Varchar",
    "Char",
    "Text",
    "Timestamp",
    "TimestampTZ",
    "Date",
    "Time",
    "TimeTZ",
    "Interval",
    "Boolean",
    "JSON",
    "JSONB",
    "Dynamic",
    "List",
]
