from toolkitorm.sql.query import BaseQuery
from toolkitorm.sql.table import BaseTable


class BaseCrate(BaseQuery):
    pass


class BaseAlter(BaseQuery):
    """Coming soon"""


class BaseDrop(BaseQuery):
    pass


__all__ = [
    "BaseCrate",
    "BaseAlter",
    "BaseDrop",
]
