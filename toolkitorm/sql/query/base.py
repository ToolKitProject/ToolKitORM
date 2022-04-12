from toolkitorm.sql.base import HasDialect, HasSQL


class BaseQuery(HasSQL, HasDialect):
    pass


__all__ = [
    "BaseQuery",
]
