import sqlite3 as sql
from datetime import datetime

from toolkitorm.orm.sqlite import Boolean, Column, Datetime, Dict, Integer, Table, Text


def connect() -> sql.Connection:
    return sql.connect("database.sqlite")


def test_storage() -> None:
    class Test(Table):
        true = Column(Boolean())
        false = Column(Boolean())
        json = Column(Dict[str]())
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
