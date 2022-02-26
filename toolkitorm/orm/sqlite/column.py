from toolkitorm.orm.sqlite.dialect import SQLiteDialect
from toolkitorm.sql.column import BaseColumn


class Column(BaseColumn):
    __dialect__ = SQLiteDialect()

__all__ = ["Column"]