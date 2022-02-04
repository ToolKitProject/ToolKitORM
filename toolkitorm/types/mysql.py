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
class Tinyint(BaseInteger):
    pass


class Smallint(BaseInteger):
    pass


class Mediumint(BaseInteger):
    pass


class Integer(BaseInteger):
    pass


class Biginteger(BaseInteger):
    pass


class Decimal(BaseDecimal):
    def __init__(self, precision: int, scale: int) -> None:
        super().__init__(precision, scale)


class Float(BaseFloat):
    pass


class Double(BaseFloat):
    pass


class Date(BaseDate):
    pass


class Time(BaseTime):
    pass


class Datetime(BaseDatetime):
    pass


class Timestamp(BaseDatetime):
    pass


class Char(BaseString):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Varchar(BaseString):
    def __init__(self, length: int) -> None:
        super().__init__(length)


class Tinytext(BaseString):
    pass


class Text(BaseString):
    pass


class Mediumtext(BaseString):
    pass


class Longtext(BaseString):
    pass


class JSON(BaseDict[_T]):
    pass


# ORM types
class Dynamic(BaseAny):
    __type_name__ = Longtext.__type_name__


class Boolean(BaseBool):
    __type_name__ = Tinyint.__type_name__


class List(BaseList[_T]):
    __type_name__ = Longtext.__type_name__


class Timedeltayt(BaseTimedelta):
    __type_name__ = Tinytext.__type_name__
