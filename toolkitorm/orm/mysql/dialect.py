from toolkitorm.sql.dialect import BaseDialect


class Dialect(BaseDialect):
    pass


class DialectMixin:
    __dialect__: BaseDialect = Dialect()


__all__ = ["Dialect", "DialectMixin"]
