import pymysql as sql


def connect() -> sql.Connection:
    return sql.connect(user="test", database="test", password="test")



