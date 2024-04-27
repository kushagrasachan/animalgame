from entity import Entity
from common.directions import Directions

class Animal(Entity):
    def __init__(self, x:int, y:int) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def move(self, direction:Directions) -> None:
        self.x += direction[0]
        self.y += direction[1]
