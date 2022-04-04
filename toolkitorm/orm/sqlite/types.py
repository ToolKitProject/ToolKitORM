from toolkitorm import V
from toolkitorm.orm.sqlite.dialect import DialectMixin
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
class Integer(BaseInteger, DialectMixin):
    pass


class Real(BaseFloat, DialectMixin):
    pass


class Text(BaseString, DialectMixin):
    pass


class Blob(BaseAny, DialectMixin):
    pass


# ORM types
class Boolean(BaseBool, DialectMixin):
    __type_name__ = Integer().__type_name__


class Decimal(BaseDecimal, DialectMixin):
    __type_name__ = Text().__type_name__


class Time(BaseTime, DialectMixin):
    __type_name__ = Text().__type_name__


class Date(BaseDate, DialectMixin):
    __type_name__ = Text().__type_name__


class Datetime(BaseDatetime, DialectMixin):
    __type_name__ = Text().__type_name__


class Timedelta(BaseTimedelta, DialectMixin):
    __type_name__ = Text().__type_name__


class Dict(BaseDict[V], DialectMixin):
    __type_name__ = Text().__type_name__


class List(BaseList[V], DialectMixin):
    __type_name__ = Text().__type_name__


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
