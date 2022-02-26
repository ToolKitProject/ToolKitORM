from toolkitorm.orm.mysql.dialect import MySQLDialect
from toolkitorm.sql.table import BaseTable


class Table(BaseTable):
    __dialect__ = MySQLDialect()


__all__ = ["Table"]
