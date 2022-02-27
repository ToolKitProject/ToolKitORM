from typing import Any


class BaseDialect:
    """
    Dialect class
    !!! ALL VALUES MUST BE UPPER CASE !!!
    """

    # Name of unsupported types (IS, IN, etc)
    UNSUPPORTED: list[str] = []

    # Escape charters
    ESCAPE: dict[int, str] = {
        0: "\\0",  # \0 (Null character)
        10: "\\n",  # \n (Line feed)
        13: "\\r",  # \r (Carriage return)
        26: "\\Z",  # \Z (Substitute character)
        34: '\\"',  # " (Quotation mark)
        39: "\\'",  # ' (Apostrophe)
        92: "\\\\",  # \ (Backslash)
    }

    STRING: str = "'"  # Used to denote strings (... VALUES ('string'))
    NAME: str = "`"  # Used to denote a SQL names (... FROM `SQL name`)

    # The first value will be used to declare,other values will be used for definitions
    TRUE: tuple[str, ...] = ("TRUE", "1")
    FALSE: tuple[str, ...] = ("FALSE", "0")
    NULL: str = "NULL"

    NOT: str = "NOT"
    AND: str = "AND"
    OR: str = "OR"

    IS: str = "IS"
    IN: str = "IN"
    EQ: str = "="
    NE: str = "!="
    GT: str = ">"
    LT: str = "<"
    GE: str = ">="
    LE: str = "<="

    def name(self, sql: str) -> str:
        return f"{self.NAME}{sql}{self.NAME}"

    def string(self, value: object) -> str:
        return f"{self.STRING}{str(value).translate(self.ESCAPE)}{self.STRING}"

    def __getattribute__(self, name: str) -> Any:
        assert name not in super().__getattribute__("UNSUPPORTED")  # TODO
        return super().__getattribute__(name)


__all__ = ["BaseDialect"]
