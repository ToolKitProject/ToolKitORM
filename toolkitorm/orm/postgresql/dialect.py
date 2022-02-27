from toolkitorm.sql.dialect import BaseDialect


class PostgreSQLDialect(BaseDialect):
    def __init__(self) -> None:
        super().__init__()

        self.NAME = '"'


__all__ = ["PostgreSQLDialect"]
