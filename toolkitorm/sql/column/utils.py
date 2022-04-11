from typing import Callable

from toolkitorm import sql
from toolkitorm.sql.column import BaseColumn


class Columns:
    table: "sql.table.BaseTable"
    all: list[BaseColumn]

    def __init__(
        self, table: "sql.table.BaseTable", columns: list[BaseColumn] = []
    ) -> None:
        self.table = table
        self.all = columns.copy()

    # Column management
    def add(self, *columns: BaseColumn) -> None:
        self.all += list(columns)

    def remove(self, *columns: BaseColumn) -> None:
        for c in columns:
            self.all.remove(c)

    def filter(
        self, func: Callable[[BaseColumn, "sql.table.BaseTable"], bool]
    ) -> "Columns":
        return Columns(self.table, [c for c in self.all if func(c, self.table)])

    # Value management
    def from_raw(self, raw: list[object]) -> None:
        assert len(raw) == len(self.all)  # TODO
        for value, column in zip(raw, self.all):
            column.data(self.table).set(value)

    def from_args_kwargs(self, *args: object, **kwargs: object) -> None:
        for num, column in enumerate(self.all):
            if column.name in kwargs:
                value = kwargs[column.name]
            elif num < len(args):
                value = args[num]
            else:
                value = column.default
            column.data(self.table).set(value)


__all__ = ["Columns"]
