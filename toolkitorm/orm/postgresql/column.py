from toolkitorm import V
from toolkitorm.orm.postgresql.dialect import DialectMixin
from toolkitorm.sql.column import BaseColumn


class Column(BaseColumn[V], DialectMixin):
    pass


__all__ = ["Column"]
