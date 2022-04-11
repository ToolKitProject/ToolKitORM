from toolkitorm import sql


def not_(c: "sql.condition.BaseCondition") -> "sql.condition.Not":
    return ~c


def and_(
    l: "sql.condition.BaseCondition", r: "sql.condition.BaseCondition"
) -> "sql.condition.And":
    return l & r


def or_(
    l: "sql.condition.BaseCondition", r: "sql.condition.BaseCondition"
) -> "sql.condition.Or":
    return l | r


__all__ = [
    "not_",
    "and_",
    "or_",
]
