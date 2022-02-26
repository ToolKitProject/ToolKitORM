from toolkitorm.sql.dialect import BaseDialect


class PostgreSQLDialect(BaseDialect):
    struct_quotes = '"'


__all__ = ["PostgreSQLDialect"]
