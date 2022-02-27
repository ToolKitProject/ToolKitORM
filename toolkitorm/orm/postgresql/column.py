from toolkitorm import V
from toolkitorm.orm.postgresql.dialect import PostgreSQLDialect
from toolkitorm.sql.column import BaseColumn


class Column(BaseColumn[V]):
    __dialect__ = PostgreSQLDialect()


__all__ = ["Column"]
