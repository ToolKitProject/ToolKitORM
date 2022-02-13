from toolkitorm.basetable import BaseTable
from toolkitorm.column import Column
from toolkitorm.columns import Columns
from toolkitorm.storage import Storage
from toolkitorm.types.mysql import Boolean


class Table(BaseTable):
    __columns__: Columns

    def __init_subclass__(cls, table: str | None = None) -> None:
        if table is not None:
            cls.__table__ = table
        else:
            cls.__table__ = cls.__name__.lower()

        return super().__init_subclass__()

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__()
        self.__storage__ = Storage()
        self.__columns__ = Columns(self)

        # Add columns
        for column in type(self).__dict__.values():
            if isinstance(column, Column):
                self.__columns__.add(column)
                self.__storage__.add(column.name, column.value_type)

        # Set values
        self.__columns__.from_args_kwargs(*args, **kwargs)


__all__ = ["Table"]
