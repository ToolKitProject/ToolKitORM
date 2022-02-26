from copy import deepcopy
from toolkitorm import V
from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.basistable import BasisTable
from toolkitorm.sql.column import BaseColumn
from toolkitorm.sql.columns import Columns


class BaseTable(BasisTable):
    """Table without dialect"""
    __columns__: Columns

    def __init_subclass__(
        cls, table: str | None = None, dialect: BaseDialect | None = None
    ) -> None:
        if table is not None:
            cls.__table__ = table
        if dialect is not None:
            cls.__dialect__ = dialect
        return super().__init_subclass__()

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__()
        self.__columns__ = Columns(self)

        # Add columns
        for column in type(self).__dict__.values():
            if isinstance(column, BaseColumn):
                assert type(column.__dialect__) is type(self.__dialect__)  # TODO
                self.__columns__.add(column)
                self.__storage__.add(column.name, column.value_type)

        # Set values
        self.__columns__.from_args_kwargs(*args, **kwargs)

    def __str__(self) -> str:
        value = f"{type(self).__name__}({self.__table__})"
        for column in self.__columns__.all:
            value += f"\n  {column.sql_name}: {column.value_type.sql_name} = {column.data(self).to_sql()}"
        return value


__all__ = ["BaseTable"]
