from arena import Arena
from element import Element
from enum import IntEnum
from random import uniform

class AppleType(IntEnum):
    GOOD_APPLE = 0
    BAD_APPLE = 1

class Apple(Element):
    apple_type: AppleType
    color: str

    def __init__(self, x: int, y: int, arena: Arena, type: AppleType,
     shape: str = "arrow", color: str = "white"):
        super().__init__(x=x, y=y, arena=arena, shape=shape, color=color)
        self.apple_type = type
    
    #Override
    def drawn(self, size: int = 15):
        super().dot(size)
    
    def randomize_location(self):
        super().undo()
        x = uniform(self.arena().arena_limit_vertex[0][0], self.arena().arena_limit_vertex[1][0])
        y = uniform(self.arena().arena_limit_vertex[0][1], self.arena().arena_limit_vertex[1][1])

        super().setpos(x, y)
        self.drawn()
