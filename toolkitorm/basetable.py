"""FIXME: DOCS"""
from toolkitorm.storage import Storage


class BaseTable:
    __table__: str
    __storage__: Storage

    def __init__(self) -> None:
        if not hasattr(self, "__table__"):
            self.__table__ = type(self).__name__.lower()
