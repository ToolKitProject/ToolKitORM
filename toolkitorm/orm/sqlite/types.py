from toolkitorm import V
from toolkitorm.orm.sqlite.dialect import SQLiteDialect
from toolkitorm.sql.dialect import BaseDialect
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


class TypeDialectMixin:
    __dialect__: BaseDialect = SQLiteDialect()


# Built-in types
class Integer(BaseInteger, TypeDialectMixin):
    pass


class Real(BaseFloat, TypeDialectMixin):
    pass


class Text(BaseString, TypeDialectMixin):
    pass


class Blob(BaseAny, TypeDialectMixin):
    pass


# ORM types
class Boolean(BaseBool, TypeDialectMixin):
    __type_name__ = Integer().__type_name__


class Decimal(BaseDecimal, TypeDialectMixin):
    __type_name__ = Text().__type_name__


class Time(BaseTime, TypeDialectMixin):
    __type_name__ = Text().__type_name__


class Date(BaseDate, TypeDialectMixin):
    __type_name__ = Text().__type_name__


class Datetime(BaseDatetime, TypeDialectMixin):
    __type_name__ = Text().__type_name__


class Timedelta(BaseTimedelta, TypeDialectMixin):
    __type_name__ = Text().__type_name__


class Dict(BaseDict[V], TypeDialectMixin):
    __type_name__ = Text().__type_name__


class List(BaseList[V], TypeDialectMixin):
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
