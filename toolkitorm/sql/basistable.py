from typing import ClassVar
from toolkitorm.sql.dialect import BaseDialect
from .storage import Storage


class BasisTable:
    __table__: str
    __storage__: Storage

    __dialect__: ClassVar[BaseDialect]

    def __init__(self) -> None:
        assert hasattr(self, "__dialect__")  # TODO
        if not hasattr(self, "__table__"):
            self.__table__ = type(self).__name__.lower()
        self.__storage__ = Storage()


__all__ = ["BasisTable"]
