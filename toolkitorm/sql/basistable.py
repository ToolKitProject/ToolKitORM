from typing import ClassVar
from toolkitorm.sql.dialect import BaseDialect
from toolkitorm.sql.storage import Storage


class BasisTable:
    __table__: str
    __storage__: Storage

    __dialect__: ClassVar[BaseDialect]

    def __init_subclass__(
        cls, table: str | None = None, dialect: BaseDialect | None = None
    ) -> None:
        if table is not None:
            cls.__table__ = table
        else:
            cls.__table__ = cls.__name__.lower()
        if dialect is not None:
            cls.__dialect__ = dialect

    def __init__(self) -> None:
        assert hasattr(self, "__dialect__")  # TODO
        self.__storage__ = Storage()

    @classmethod
    @property
    def sql_name(cls) -> str:
        return cls.__dialect__.name(cls.__table__)


__all__ = ["BasisTable"]
