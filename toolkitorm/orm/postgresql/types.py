from toolkitorm import V
from toolkitorm.orm.postgresql.dialect import PostgreSQLDialect
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
    __dialect__: BaseDialect = PostgreSQLDialect()


# Built-in types
class Smallint(BaseInteger, TypeDialectMixin):
    pass


class Integer(BaseInteger, TypeDialectMixin):
    pass


class Bigint(BaseInteger, TypeDialectMixin):
    pass


class Decimal(BaseDecimal, TypeDialectMixin):
    def __init__(self, precision: int, scale: int) -> None:
        super().__init__(precision, scale)


class Real(BaseFloat, TypeDialectMixin):
    pass


class Double(BaseFloat, TypeDialectMixin):
    __type_name__ = "double precision"


class Varchar(BaseString, TypeDialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Char(BaseString, TypeDialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Text(BaseString, TypeDialectMixin):
    pass


class Timestamp(BaseDatetime, TypeDialectMixin):
    pass


class TimestampTZ(BaseDatetime, TypeDialectMixin):
    pass


class Date(BaseDate, TypeDialectMixin):
    pass


class Time(BaseTime, TypeDialectMixin):
    pass


class TimeTZ(BaseTime, TypeDialectMixin):
    pass


class Interval(BaseTimedelta, TypeDialectMixin):
    pass


class Boolean(BaseBool, TypeDialectMixin):
    pass


class JSON(BaseDict[V], TypeDialectMixin):
    pass


class JSONB(BaseDict[V], TypeDialectMixin):
    pass


# ORM types
class Dynamic(BaseAny, TypeDialectMixin):
    __type_name__ = Text().__type_name__


class List(BaseList[V], TypeDialectMixin):
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
