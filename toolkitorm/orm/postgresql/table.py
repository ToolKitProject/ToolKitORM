from toolkitorm.orm.postgresql.dialect import DialectMixin
from toolkitorm.sql.table import BaseTable


class Table(BaseTable, DialectMixin):
    pass


__all__ = ["Table"]
