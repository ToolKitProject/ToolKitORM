from datetime import datetime

from pymysql import connect

from toolkitorm.orm.mysql import JSON, Boolean, Column, Datetime, Integer, Table, Text
from toolkitorm.request.manager import Manager

manager = Manager(connect, user="test", database="test", password="test")


def test_connect() -> None:
    with manager.connect() as session:
        session("CREATE TABLE IF NOT EXISTS test (test INTEGER)")
        session("DROP TABLE IF EXISTS test")


def test_storage() -> None:
    class Test(Table):
        true = Column(Boolean())
        false = Column(Boolean())
        json = Column(JSON[str]())
        dt = Column(Datetime())
        num = Column(Integer())
        txt = Column(Text())

    t = Test("TrUe", "0", '{"a":123}', "2001-09-11 05:05:00", "456231", 123)
    assert t.true is True
    assert t.false is False
    assert t.json == {"a": 123}
    assert t.dt == datetime.fromisoformat("2001-09-11 05:05:00")
    assert t.num == 456231
    assert t.txt == "123"
