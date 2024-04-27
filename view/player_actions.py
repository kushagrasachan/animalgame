from enum import Enum, auto
import curses

class PlayerActions(Enum):
    MOVE_PLAYER_RIGHT = auto()
    MOVE_PLAYER_LEFT = auto()
    SHOOT = auto()

    PAUSE_GAME = auto()
    QUIT_GAME = auto()

    NOTHING = auto()
    MISCLICKED = auto()