from toolkitorm.basetable import BaseTable
from toolkitorm.column import Column
from toolkitorm.storage import Storage
from toolkitorm.types.mysql import Boolean


class Table(BaseTable):
    __columns__: list[Column]

    def __init_subclass__(cls, table: str | None = None) -> None:
        if table is not None:
            cls.__table__ = table
        else:
            cls.__table__ = cls.__name__.lower()

        return super().__init_subclass__()

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__()
        self.__storage__ = Storage()
        self.__columns__ = []

        num = 0
        for name, column in type(self).__dict__.items():
            if isinstance(column, Column):
                self.__columns__.append(column)
                if name in kwargs:
                    value = kwargs[name]
                elif num < len(args):
                    value = args[num]
                else:
                    value = column.default
                self.__storage__.add(column.name, value, column.value_type)
                num += 1


__all__ = ["Table"]
