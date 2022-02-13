from copy import deepcopy
from typing import Callable
from toolkitorm.basetable import BaseTable
from toolkitorm.column import Column


class Columns:
    table: BaseTable
    columns: list[Column]

    def __init__(self, table: BaseTable, columns: list[Column] = []) -> None:
        self.table = table
        self.columns = deepcopy(columns)

    # Column management
    def add(self, *columns: Column) -> None:
        self.columns += list(columns)

    def remove(self, *columns: Column) -> None:
        for c in columns:
            self.columns.remove(c)

    def filter(self, func: Callable[[Column, BaseTable], bool]) -> "Columns":
        return Columns(self.table, [c for c in self.columns if func(c, self.table)])

    # Value management
    def from_raw(self, raw: list[object]) -> None:
        assert len(raw) == len(self.columns)  # TODO
        for value, column in zip(raw, self.columns):
            column.data(self.table).set(value)

    def from_args_kwargs(self, *args: object, **kwargs: object) -> None:
        for num, column in enumerate(self.columns):
            if column.name in kwargs:
                value = kwargs[column.name]
            elif num < len(args):
                value = args[num]
            else:
                value = column.default
            column.data(self.table).set(value)


__all__ = ["Columns"]
