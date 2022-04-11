from toolkitorm import V
from toolkitorm.sql.storage.data import Data
from toolkitorm.sql.types.base import BaseType


class Storage:
    storage: dict[str, Data]

    def __init__(self) -> None:
        self.storage = {}

    def get(self, name: str) -> Data:
        assert name in self.storage, "Column not found"  # TODO
        return self.storage[name]

    def add(self, name: str, value_type: BaseType[V]) -> None:
        assert name not in self.storage, "Column already exist"  # TODO
        self.storage[name] = Data(value_type)


__all__ = ["Storage"]
