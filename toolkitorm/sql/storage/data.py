from typing import Generic

from toolkitorm import V
from toolkitorm.sql.types.base import BaseType


class Data(Generic[V]):
    value_type: BaseType[V]
    value: V | None

    def __init__(self, value_type: BaseType[V], value: object = None) -> None:
        self.value_type = value_type
        self.set(value)

    def get(self) -> V | None:
        return self.value

    def set(self, value: object) -> None:
        self.value = self.value_type.convert(value)

    def to_sql(self) -> str:
        return self.value_type.to_sql(self.value)


__all__ = ["Data"]
