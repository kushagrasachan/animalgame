from entity import Entity
from common.directions import Directions

class Fire(Entity):
    def __init__(self) -> None:
        super().__init__()

    def move(self, direction:Directions) -> None:
        self.x += direction[0]
        self.y += direction[1]
