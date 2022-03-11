from typing import Any, Literal

from toolkitorm import V
from toolkitorm.request.cursor import Cursor


class Session:
    __connection: Any

    def __init__(self, connection: Any) -> None:
        self.__connection = connection

    def __enter__(self) -> "Session":
        return self

    def __exit__(self, *args: object) -> Literal[False]:
        return False

    def close(self) -> None:
        self.__connection.close()

    def commit(self) -> None:
        self.__connection.commit()

    def rollback(self) -> None:
        self.__connection.rollback()

    def cursor(self) -> Cursor:
        return Cursor(self.__connection.cursor())

    def execute(self, sql: str) -> None:
        with self.cursor() as cursor:
            cursor(sql)

    def one(self, sql: str) -> tuple[V] | None:
        with self.cursor() as cursor:
            return cursor(sql).one()

    def many(self, sql: str, size: int) -> list[tuple[V]]:
        with self.cursor() as cursor:
            return cursor(sql).many(size)

    def all(self, sql: str) -> list[tuple[V]]:
        with self.cursor() as cursor:
            return cursor(sql).all()

    __call__ = execute


__all__ = ["Session"]
