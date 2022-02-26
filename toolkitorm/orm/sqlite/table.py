from toolkitorm.orm.sqlite.dialect import SQLiteDialect
from toolkitorm.sql.table import BaseTable


class Table(BaseTable):
    __dialect__ = SQLiteDialect()


__all__ = ["Table"]
