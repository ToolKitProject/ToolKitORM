from toolkitorm.sql.column import BaseColumn, Columns
from toolkitorm.sql.operator import BaseCondition
from toolkitorm.sql.query import BaseQuery
from toolkitorm.sql.table import BaseTable


class BaseSelect(BaseQuery):
    # TODO: join and table list

    def __init__(self) -> None:
        super().__init__(
            [
                "select",
                "from",
            ],
            [
                "select",
                "from",
                "where",
                "order",
                "limit",
                "group",
                "having",
            ],
        )

    def select(self, columns: Columns, distinct: bool = False) -> "BaseSelect":
        self.add(
            "select",
            f'{"SELECT DISTINCT" if distinct else "SELECT ALL"} {columns.names()}',
        )
        return self

    def from_(self, table: type[BaseTable]) -> "BaseSelect":
        self.add("from", f"FROM {table.sql_name()}")
        return self

    def where(self, condition: BaseCondition) -> "BaseSelect":
        self.add("where", f"WHERE {condition.to_sql()}")
        return self

    def order(self, column: BaseColumn) -> "BaseSelect":
        self.add("order", f"ORDER BY {column.sql_name()}")
        return self

    def limit(self, limit: int, offset: int = 0) -> "BaseSelect":
        self.add("limit", f"LIMIT {limit} OFFSET {offset}")
        return self

    def group(self, column: BaseColumn) -> "BaseSelect":
        self.__body["group"] = f"GROUP BY {column.sql_name()}"
        return self

    def having(self, condition: BaseCondition) -> "BaseSelect":
        self.__body["having"] = f"HAVING {condition.to_sql()}"
        return self


class BaseInsert(BaseQuery):
    def __init__(self) -> None:
        super().__init__(
            [
                "insert",
            ],
            [
                "insert",
                "returning",
            ],
        )

    def insert(self, table: type[BaseTable], columns: Columns) -> "BaseInsert":
        self.add(
            "insert",
            f"INSERT INTO {table.sql_name()}({columns.names()}) VALUES ({columns.values()})",
        )
        return self

    def returning(self, columns: Columns) -> "BaseInsert":
        self.add("returning", f"RETURNING {columns.names()}")
        return self


class BaseUpdate(BaseQuery):
    def __init__(self) -> None:
        super().__init__(
            [
                "update",
                "set",
            ],
            [
                "update",
                "set",
                "where",
                "returning",
            ],
        )

    def update(self, table: type[BaseTable]) -> "BaseUpdate":
        self.add("update", f"UPDATE {table.sql_name()}")
        return self

    def set_(self, columns: Columns) -> "BaseUpdate":
        self.add(
            "set",
            f'SET {columns.format(lambda c, t: f"{c.sql_name()}={c.data(t).to_sql()}")}',
        )

        return self

    def where(self, condition: BaseCondition) -> "BaseUpdate":
        self.add("where", f"WHERE {condition.to_sql()}")
        return self

    def returning(self, columns: Columns) -> "BaseUpdate":
        self.add("returning", f"RETURNING {columns.names()}")
        return self


class BaseDelete(BaseQuery):
    def __init__(self) -> None:
        super().__init__(["delete"], ["delete", "where"])

    def delete(self, table: type[BaseTable]) -> "BaseDelete":
        self.add("delete", f"DELETE FROM {table.sql_name()}")
        return self

    def where(self, condition: BaseCondition) -> "BaseDelete":
        self.add("where", f"WHERE {condition.to_sql()}")
        return self


__all__ = [
    "BaseSlect",
    "BaseInsert",
    "BaseUpdate",
    "BaseDelete",
]
