from typing import Generic

from toolkitorm import SQL, V
from toolkitorm.sql.types import BaseType


class Data(Generic[V]):
    value: V | None
    value_type: BaseType[V]

    def __init__(self, value_type: BaseType[V]) -> None:
        self.value = None
        self.value_type = value_type

    def to_sql(self) -> SQL:
        return self.value_type.to_sql(self.value)

    def to_python(self) -> V | None:
        return self.value

    def set(self, value: object) -> None:
        self.value = self.value_type.convert(value)


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


__all__ = ["Data", "Storage"]
