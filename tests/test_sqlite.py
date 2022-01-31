import sqlite3 as sql


def connect() -> sql.Connection:
    return sql.connect("database.sqlite")
