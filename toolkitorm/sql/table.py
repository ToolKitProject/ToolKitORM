from toolkitorm.sql.base import HasDialect, HasName
from toolkitorm.sql.column import BaseColumn, Columns
from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.storage import Storage


class BaseTable(HasName, HasDialect):
    __table__: str
    __storage__: Storage
    __columns__: Columns

    def __init_subclass__(
        cls, table: str | None = None, dialect: BaseDialect | None = None
    ) -> None:
        if table is not None:
            cls.__table__ = table
        else:
            cls.__table__ = cls.__name__.lower()

        if dialect is not None:
            cls.__dialect__ = dialect

    def __init__(self, *args: object, **kwargs: object) -> None:
        assert hasattr(self, "__dialect__")  # TODO
        self.__storage__ = Storage()
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
        return f"<{type(self).__name__} ({self.sql_name()})>"

    @classmethod
    def sql_name(cls) -> str:
        return cls.__dialect__.name(cls.__table__)


__all__ = [
    "BaseTable",
]
