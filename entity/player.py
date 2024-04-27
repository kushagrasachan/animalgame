from entity import Entity
from common.directions import Directions
from common import config

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# try:
#     from model import Model       ##just implementing this code gave a circular import error
# except ImportError:
#     import sys
#     Model = sys.modules['model' + '.Model']

class Player(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.x = int(config.TERM_WIDTH/2)
        self.y = config.TERM_HEIGHT-2

    def move(self, direction) -> None:
        # logger.info(f"{direction}")
        # logger.info(f"{direction[0], direction[1]}")
        if direction == Directions.LEFT:
            self.x -= 1
        if direction == Directions.RIGHT:
            self.x += 1

    def shoot(self, model) -> None:
        model.add_fire()
        pass
