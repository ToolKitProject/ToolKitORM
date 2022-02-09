"""FIXME: DOCS"""
from typing import Generic, Optional

from toolkitorm.types.base import BaseType, V


class BaseColumn(Generic[V]):
    name: str
    value_type: BaseType[V]
    default: V | None
    nullable: bool
    auto: bool
    unique: bool
    primary: bool
    foreign: Optional["BaseColumn[V]"]

    def __init__(
        self,
        value_type: BaseType[V],
        default: V | None = None,
        nullable: bool = False,
        auto: bool = False,
        unique: bool = False,
        primary: bool = False,
        foreign: Optional["BaseColumn[V]"] = None,
    ) -> None:
        self.value_type = value_type
        self.default = default
        self.nullable = nullable
        self.auto = auto
        self.unique = unique
        self.primary = primary
        self.foreign = foreign

        if self.auto:
            self.nullable = True
        if self.primary:
            self.nullable = True
            self.unique = True

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name


class Column(BaseColumn[V]):
    pass


class OptionalColumn(BaseColumn[V | None]):
    pass
