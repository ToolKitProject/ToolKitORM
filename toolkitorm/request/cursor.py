from typing import Any, Literal
from toolkitorm import V


class Cursor:
    __cursor: Any

    def __init__(self, cursor: Any) -> None:
        self.__cursor = cursor

    def __enter__(self) -> "Cursor":
        return self

    def __exit__(self, *args: object) -> Literal[False]:
        self.close()
        return False

    def close(self) -> None:
        self.__cursor.close()

    def execute(self, sql: str) -> "Cursor":
        self.__cursor.execute(sql)
        return self

    def one(self) -> tuple[V] | None:
        return self.__cursor.fetchone()

    def many(self, size: int) -> list[tuple[V]]:
        return self.__cursor.fetchmany(size)

    def all(self) -> list[tuple[V]]:
        return self.__cursor.fetchall()

    __call__ = execute


__all__ = ["Cursor"]
