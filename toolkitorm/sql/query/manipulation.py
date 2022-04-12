from toolkitorm.sql.query import BaseQuery


class BaseSelect(BaseQuery):
    pass


class BaseInsert(BaseQuery):
    pass


class BaseUpdate(BaseQuery):
    pass


class BaseDelete(BaseQuery):
    pass


__all__ = [
    "BaseSlect",
    "BaseInsert",
    "BaseUpdate",
    "BaseDelete",
]
