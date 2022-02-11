from datetime import datetime

import pg8000 as sql
from toolkitorm.column import Column
from toolkitorm.storage import Storage
from toolkitorm.table import Table
from toolkitorm.types.postgresql import JSON, Boolean, Integer, Text, Timestamp


def connect() -> sql.Connection:
    return sql.connect(user="test", database="test", password="test")


def test_storage() -> None:
    class Test(Table):
        true = Column(Boolean())
        false = Column(Boolean())
        json = Column(JSON[str]())
        dt = Column(Timestamp())
        num = Column(Integer())
        txt = Column(Text())

    t = Test("TrUe", "0", '{"a":123}', "2001-09-11 05:05:00", "456231", 123)
    assert t.true is True
    assert t.false is False
    assert t.json == {"a": 123}
    assert t.dt == datetime.fromisoformat("2001-09-11 05:05:00")
    assert t.num == 456231
    assert t.txt == "123"
