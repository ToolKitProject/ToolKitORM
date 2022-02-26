from toolkitorm.orm.postgresql.dialect import PostgreSQLDialect
from toolkitorm.sql.table import BaseTable


class Table(BaseTable):
    __dialect__ = PostgreSQLDialect()


__all__ = ["Table"]
