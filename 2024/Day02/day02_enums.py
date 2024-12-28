from enum import Enum, auto


class ReactorState(Enum):
    START = auto()
    POSITIVE = auto()
    NEGATIVE = auto()
    NEUTRAL = auto()
