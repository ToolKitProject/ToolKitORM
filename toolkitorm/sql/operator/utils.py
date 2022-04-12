from toolkitorm import sql


def not_(c: "sql.operator.BaseCondition") -> "sql.operator.Not":
    return ~c


def and_(
    l: "sql.operator.BaseCondition", r: "sql.operator.BaseCondition"
) -> "sql.operator.And":
    return l & r


def or_(
    l: "sql.operator.BaseCondition", r: "sql.operator.BaseCondition"
) -> "sql.operator.Or":
    return l | r


__all__ = [
    "not_",
    "and_",
    "or_",
]
