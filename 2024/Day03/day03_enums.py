from enum import Enum, auto


class NumberParsingState(Enum):
    INIT = auto()
    FIRST_NUM = auto()
    SECOND_NUM = auto()
    END = auto()

class MulParsingState(Enum):
    INIT = auto()
    M = auto()
    U = auto()
    L = auto()
    PAREN = auto()
    D = auto()
    O = auto()
    N = auto()
    SINGLE_QUOTE = auto()
    T = auto()
    DO_PAREN = auto()
    DONT_PAREN = auto()

class ConditionalParsingState(Enum):
    DO = auto()
    DONT = auto()
