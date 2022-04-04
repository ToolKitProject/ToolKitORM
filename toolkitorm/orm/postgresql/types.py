from toolkitorm import V
from toolkitorm.orm.postgresql.dialect import DialectMixin
from toolkitorm.sql.types import (
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
class Smallint(BaseInteger, DialectMixin):
    pass


class Integer(BaseInteger, DialectMixin):
    pass


class Bigint(BaseInteger, DialectMixin):
    pass


class Decimal(BaseDecimal, DialectMixin):
    def __init__(self, precision: int, scale: int) -> None:
        super().__init__(precision, scale)


class Real(BaseFloat, DialectMixin):
    pass


class Double(BaseFloat, DialectMixin):
    __type_name__ = "double precision"


class Varchar(BaseString, DialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Char(BaseString, DialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Text(BaseString, DialectMixin):
    pass


class Timestamp(BaseDatetime, DialectMixin):
    pass


class TimestampTZ(BaseDatetime, DialectMixin):
    pass


class Date(BaseDate, DialectMixin):
    pass


class Time(BaseTime, DialectMixin):
    pass


class TimeTZ(BaseTime, DialectMixin):
    pass


class Interval(BaseTimedelta, DialectMixin):
    pass


class Boolean(BaseBool, DialectMixin):
    pass


class JSON(BaseDict[V], DialectMixin):
    pass


class JSONB(BaseDict[V], DialectMixin):
    pass


# ORM types
class Dynamic(BaseAny, DialectMixin):
    __type_name__ = Text().__type_name__


class List(BaseList[V], DialectMixin):
    __type_name__ = Text().__type_name__


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
