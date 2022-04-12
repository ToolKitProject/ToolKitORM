from toolkitorm.sql.dialect import BaseDialect, BaseDialectMixin


class Dialect(BaseDialect):
    def __init__(self) -> None:
        super().__init__()

        self.NAME = '"'


class DialectMixin(BaseDialectMixin):
    __dialect__ = Dialect()


__all__ = [
    "Dialect",
    "DialectMixin",
]
