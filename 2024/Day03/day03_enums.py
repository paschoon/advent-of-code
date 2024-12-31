from enum import Enum, auto


class ParsingState(Enum):
    INIT = auto()
    FIRST_NUM = auto()
    SECOND_NUM = auto()
    END = auto()
