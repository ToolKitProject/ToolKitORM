from toolkitorm.sql.dialect import BaseDialect, BaseDialectMixin


class Dialect(BaseDialect):
    pass


class DialectMixin(BaseDialectMixin):
    __dialect__ = Dialect()


__all__ = [
    "Dialect",
    "DialectMixin",
]
