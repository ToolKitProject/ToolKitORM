from toolkitorm.sql.condition import BaseCondition, Logical
from toolkitorm.sql.dialect import BaseDialect


class Not(BaseCondition):
    action: str
    condition: BaseCondition

    def __init__(self, dialect: BaseDialect, c: BaseCondition) -> None:
        super().__init__(dialect)
        self.action = dialect.NOT
        self.condition = c

    def to_sql(self) -> str:
        return f"{self.action} ({self.condition.to_sql()})"


class And(Logical):
    def __init__(self, dialect: BaseDialect, l: BaseCondition, r: BaseCondition) -> None:
        super().__init__(dialect, l, dialect.AND, r)


class Or(Logical):
    def __init__(self, dialect: BaseDialect, l: BaseCondition, r: BaseCondition) -> None:
        super().__init__(dialect, l, dialect.OR, r)


__all__ = ["Not", "And", "Or"]
