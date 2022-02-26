from toolkitorm.orm.mysql.dialect import MySQLDialect
from toolkitorm.sql.column import BaseColumn


class Column(BaseColumn):
    __dialect__ = MySQLDialect()


__all__ = ["Column"]
