from toolkitorm import V
from toolkitorm.orm.mysql.dialect import DialectMixin
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
class Tinyint(BaseInteger, DialectMixin):
    pass


class Smallint(BaseInteger, DialectMixin):
    pass


class Mediumint(BaseInteger, DialectMixin):
    pass


class Integer(BaseInteger, DialectMixin):
    pass


class Biginteger(BaseInteger, DialectMixin):
    pass


class Decimal(BaseDecimal, DialectMixin):
    def __init__(self, precision: int, scale: int) -> None:
        super().__init__(precision, scale)


class Float(BaseFloat, DialectMixin):
    pass


class Double(BaseFloat, DialectMixin):
    pass


class Date(BaseDate, DialectMixin):
    pass


class Time(BaseTime, DialectMixin):
    pass


class Datetime(BaseDatetime, DialectMixin):
    pass


class Timestamp(BaseDatetime, DialectMixin):
    pass


class Char(BaseString, DialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Varchar(BaseString, DialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Tinytext(BaseString, DialectMixin):
    pass


class Text(BaseString, DialectMixin):
    pass


class Mediumtext(BaseString, DialectMixin):
    pass


class Longtext(BaseString, DialectMixin):
    pass


class JSON(BaseDict[V], DialectMixin):
    pass


# ORM types
class Dynamic(BaseAny, DialectMixin):
    __type_name__ = Longtext().__type_name__


class Boolean(BaseBool, DialectMixin):
    __type_name__ = Tinyint().__type_name__


class List(BaseList[V], DialectMixin):
    __type_name__ = Longtext().__type_name__


class Timedelta(BaseTimedelta, DialectMixin):
    __type_name__ = Tinytext().__type_name__


__all__ = [
    "Tinyint",
    "Smallint",
    "Mediumint",
    "Integer",
    "Biginteger",
    "Decimal",
    "Float",
    "Double",
    "Date",
    "Time",
    "Datetime",
    "Timestamp",
    "Char",
    "Varchar",
    "Tinytext",
    "Text",
    "Mediumtext",
    "Longtext",
    "JSON",
    "Dynamic",
    "Boolean",
    "List",
    "Timedelta",
]
