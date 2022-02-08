import sqlite3 as sql
from datetime import datetime

from toolkitorm.storage import Storage
from toolkitorm.types.sqlite import Boolean, Datetime, Dict, Integer, Text


def connect() -> sql.Connection:
    return sql.connect("database.sqlite")


def test_storage() -> None:
    s = Storage()

    s.add("True", "TrUe", Boolean())
    s.add("False", "no", Boolean())
    s.add("0", "0", Boolean())
    s.add("Dict", '{"t":null,"0":true}', Dict())
    s.add("Datetime", "2005-08-09 18:31:42", Datetime())
    s.add("Integer", "168", Integer())
    s.add("Text", 123, Text())

    assert s.get("True").value is True
    assert s.get("False").value is False
    assert s.get("0").value is False
    assert s.get("Dict").value == {"t": None, "0": True}
    assert s.get("Datetime").value == datetime.fromisoformat("2005-08-09 18:31:42")
    assert s.get("Integer").value == 168
    assert s.get("Text").value == "123"
