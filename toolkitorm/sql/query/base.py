from toolkitorm.sql.base import HasDialect, HasSQL


class BaseQuery(HasSQL, HasDialect):
    __body: dict[str, str]
    __required: list[str]
    __order: list[str]

    def __init__(self, required: list[str], order: list[str]) -> None:
        self.__body = {}
        self.__required = required
        self.__order = order

    def is_full(self) -> bool:
        return all([r in self.__body for r in self.__required])

    def add(self, key: str, value: str) -> "BaseQuery":
        self.__body[key] = value
        return self

    def to_sql(self) -> str:
        assert self.is_full()  # TODO
        c = []
        for k in self.__order:
            if k in self.__body:
                c.append(self.__body[k])
        return " ".join(c)


__all__ = [
    "BaseQuery",
]
