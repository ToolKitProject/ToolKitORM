from toolkitorm.sql.dialect import BaseDialect


class Dialect(BaseDialect):
    def __init__(self) -> None:
        super().__init__()

        self.NAME = '"'


class DialectMixin:
    __dialect__: BaseDialect = Dialect()


__all__ = ["Dialect", "DialectMixin"]
