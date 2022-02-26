from toolkitorm import SQL


class BaseDialect:
    struct_quotes: str = "`"  # Used to denote a SQL structure (DROP TABLE `SQL struct`)

    and_: SQL = SQL(" AND ")
    or_: SQL = SQL(" OR ")
    eq: SQL = SQL("==")
    ne: SQL = SQL("!=")
    gt: SQL = SQL(">")
    lt: SQL = SQL("<")
    ge: SQL = SQL(">=")
    le: SQL = SQL("<=")

    @classmethod
    def struct(cls, sql: SQL) -> SQL:
        return SQL(f"{cls.struct_quotes}{sql}{cls.struct_quotes}")


__all__ = ["BaseDialect"]
