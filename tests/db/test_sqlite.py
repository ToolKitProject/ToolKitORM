from datetime import datetime
from sqlite3 import connect

from toolkitorm.db.factory import SessionFactory
from toolkitorm.orm.sqlite import (
    Boolean,
    Column,
    Datetime,
    Dict,
    Integer,
    Table,
    Text,
    and_,
    not_,
    or_,
)

factory = SessionFactory(connect, "database.sqlite")


class TableTest(Table, table="test"):
    true = Column(Boolean())
    false = Column(Boolean())
    json = Column(Dict[str]())
    dt = Column(Datetime())
    num = Column(Integer())
    txt = Column(Text())


def test_connect() -> None:
    with factory.create() as session:
        session.execute("CREATE TABLE IF NOT EXISTS test (test INTEGER)")
        session.execute("DROP TABLE IF EXISTS test")


def test_storage() -> None:
    t = TableTest("TrUe", "0", '{"a":123}', "2001-09-11 05:05:00", "456231", 123)
    assert t.true is True
    assert t.false is False
    assert t.json == {"a": 123}
    assert t.dt == datetime.fromisoformat("2001-09-11 05:05:00")
    assert t.num == 456231
    assert t.txt == "123"


def test_conditions() -> None:
    assert str(TableTest.num == 1) == "`test`.`num` = 1"
    assert str(TableTest.num != 1) == "`test`.`num` != 1"
    assert str(TableTest.num > 1) == "`test`.`num` > 1"
    assert str(TableTest.num < 1) == "`test`.`num` < 1"
    assert str(TableTest.num >= 1) == "`test`.`num` >= 1"
    assert str(TableTest.num <= 1) == "`test`.`num` <= 1"
    assert str(TableTest.num.IN(1, 2, 3, 4, 5)) == "`test`.`num` IN (1,2,3,4,5)"
    assert str(TableTest.num.IS("null")) == "`test`.`num` IS NULL"

    assert str(not_(TableTest.num == 1)) == "NOT (`test`.`num` = 1)"
    assert (
        str(and_(TableTest.num == 1, TableTest.num == 2))
        == "(`test`.`num` = 1) AND (`test`.`num` = 2)"
    )
    assert (
        str(or_(TableTest.num == 1, TableTest.num == 2))
        == "(`test`.`num` = 1) OR (`test`.`num` = 2)"
    )
