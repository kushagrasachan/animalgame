from entity import Entity
from common.directions import Directions
# import model
from common import config

# try:
#     from model import Model       ##just implementing this code gave a circular import error
# except ImportError:
#     import sys
#     Model = sys.modules['model' + '.Model']

class Player(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.x = config.TERM_WIDTH/2
        self.y = config.TERM_HEIGHT

    def move(self, direction:Directions) -> None:
        self.x += direction[0]
        self.y += direction[1]

    def shoot(self, model) -> None:
        # model.add_fire()
        pass
