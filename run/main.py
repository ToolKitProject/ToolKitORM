from datetime import datetime

from toolkitorm.orm.postgresql import (
    JSON,
    Boolean,
    Column,
    Integer,
    Table,
    Text,
    Timestamp,
)
from toolkitorm.orm.sqlite import Column as SQLITE, Blob


def main() -> None:
    class Test(Table):
        true = Column(Boolean())
        false = Column(Boolean())
        json = Column(JSON[str]())
        dt = Column(Timestamp())
        num = Column(Integer())
        txt = Column(Text())
        sqlite = SQLITE(Blob())

    t = Test(True, False, {"a": None}, datetime.now(), "456231", 123)
    print(t)
    print(Test.num >= 123)


if __name__ == "__main__":
    main()
