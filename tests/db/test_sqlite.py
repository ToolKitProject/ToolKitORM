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
)

factory = SessionFactory(connect, "database.sqlite")


class Test(Table):
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
    t = Test("TrUe", "0", '{"a":123}', "2001-09-11 05:05:00", "456231", 123)
    assert t.true is True
    assert t.false is False
    assert t.json == {"a": 123}
    assert t.dt == datetime.fromisoformat("2001-09-11 05:05:00")
    assert t.num == 456231
    assert t.txt == "123"


def test_conditions() -> None:
    assert (
        str(not_(and_(Test.num >= 10, Test.txt.IN("test", 123))))
        == "NOT (`test`.`num` >= 10 AND `test`.`txt` IN ('test','123'))"
    )
