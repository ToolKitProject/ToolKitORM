from toolkitorm import V
from toolkitorm.orm.mysql.dialect import MySQLDialect
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
    __dialect__: BaseDialect = MySQLDialect()


# Built-in types
class Tinyint(BaseInteger, TypeDialectMixin):
    pass


class Smallint(BaseInteger, TypeDialectMixin):
    pass


class Mediumint(BaseInteger, TypeDialectMixin):
    pass


class Integer(BaseInteger, TypeDialectMixin):
    pass


class Biginteger(BaseInteger, TypeDialectMixin):
    pass


class Decimal(BaseDecimal, TypeDialectMixin):
    def __init__(self, precision: int, scale: int) -> None:
        super().__init__(precision, scale)


class Float(BaseFloat, TypeDialectMixin):
    pass


class Double(BaseFloat, TypeDialectMixin):
    pass


class Date(BaseDate, TypeDialectMixin):
    pass


class Time(BaseTime, TypeDialectMixin):
    pass


class Datetime(BaseDatetime, TypeDialectMixin):
    pass


class Timestamp(BaseDatetime, TypeDialectMixin):
    pass


class Char(BaseString, TypeDialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Varchar(BaseString, TypeDialectMixin):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Tinytext(BaseString, TypeDialectMixin):
    pass


class Text(BaseString, TypeDialectMixin):
    pass


class Mediumtext(BaseString, TypeDialectMixin):
    pass


class Longtext(BaseString, TypeDialectMixin):
    pass


class JSON(BaseDict[V], TypeDialectMixin):
    pass


# ORM types
class Dynamic(BaseAny, TypeDialectMixin):
    __type_name__ = Longtext().__type_name__


class Boolean(BaseBool, TypeDialectMixin):
    __type_name__ = Tinyint().__type_name__


class List(BaseList[V], TypeDialectMixin):
    __type_name__ = Longtext().__type_name__


class Timedelta(BaseTimedelta, TypeDialectMixin):
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
