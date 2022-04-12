from toolkitorm.sql.base import HasDialect
from toolkitorm.sql.dialect import BaseDialect


class BaseDialectMixin(HasDialect):
    __dialect__ = BaseDialect()


__all__ = [
    "BaseDialectMixin",
]
