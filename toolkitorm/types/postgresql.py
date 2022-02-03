from toolkitorm.types.base import (
    BaseAny,
    BaseInteger,
    BaseFloat,
    BaseDecimal,
    BaseString,
    BaseBytes,
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
class Smallint(BaseInteger):
    pass


class Integer(BaseInteger):
    pass


class Bigint(BaseInteger):
    pass


class Decimal(BaseDecimal):
    def __init__(self, precision: int, scale: int) -> None:
        super().__init__(precision, scale)


class Numeric(Decimal):
    pass


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


class ByteA(BaseBytes):
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
class List(BaseList[_T]):
    pass


class Dynamic(BaseAny):
    pass
