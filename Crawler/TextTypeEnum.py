import enum

class TextType(enum.Enum):
    LINK = "link"
    DATE = "date"
    TEXT = "text"
    INT = "int"
    STRING = "string"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"