from collections.abc import Callable
from typing import Any, Literal, NoReturn

from toolkitorm.request.session import Session


class Manager:
    # Connection constructor from any module with DB API v2.0 support
    __connector: Callable | NoReturn  # https://github.com/python/mypy/issues/708
    args: tuple[Any, ...]
    kwargs: dict[str, Any]

    def __init__(
        self,
        connector: Callable,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.__connector = connector
        self.args = args
        self.kwargs = kwargs

    def connect(self) -> Session:
        return Session(self.__connector(*self.args, **self.kwargs))

    def __enter__(self) -> "Manager":
        return self

    def __exit__(self, *args: object) -> Literal[True]:
        return True


__all__ = ["Manager"]
