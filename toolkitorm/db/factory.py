from collections.abc import Callable
from typing import Any, Literal, NoReturn

from toolkitorm.db.session import Session


class SessionFactory:
    # Connection constructor from any module with DB API v2.0 support
    __connector: Callable | NoReturn  # https://github.com/python/mypy/issues/708
    __args: tuple[Any, ...]
    __kwargs: dict[str, Any]

    def __init__(
        self,
        connector: Callable,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.__connector = connector
        self.__args = args
        self.__kwargs = kwargs

    def create(self) -> Session:
        return Session(self.__connector(*self.__args, **self.__kwargs))


__all__ = [
    "SessionFactory",
]
