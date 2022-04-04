from datetime import datetime

from pg8000 import connect

from toolkitorm.db.factory import SessionFactory
from toolkitorm.orm.postgresql import (
    JSON,
    Boolean,
    Column,
    Integer,
    Table,
    Text,
    Timestamp,
    and_,
    not_,
)

factory = SessionFactory(connect, user="test", database="test", password="test")


class Test(Table):
    true = Column(Boolean())
    false = Column(Boolean())
    json = Column(JSON[str]())
    dt = Column(Timestamp())
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
        not_(and_(Test.num >= 10, Test.txt.IN("test", 123))).to_sql()
        == 'NOT ("test"."num" >= 10 AND "test"."txt" IN (\'test\',\'123\'))'
    )
