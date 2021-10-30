import turtle
from apple import Apple, AppleType
from arena import Arena
from cosnts import Consts
from element import Element

class Player(Element):
    velocity = 5
    hp = 3
    score = 0

    def __init__(self, x: int, y: int, arena: Arena, shape: str = "arrow", color: str = "white"):
        super().__init__(x=x, y=y, arena=arena, shape=shape, color=color)

    #region Player input----------------------------------------------------------------------------
    def go_forward(self):
        if(self.arena().check_arena_bounds(self) == 2): return
        super().setheading(90)
        super().forward(self.velocity)
        self.check_collision()
    def go_left(self):
        if(self.arena().check_arena_bounds(self) == 1): return
        super().setheading(180)
        super().forward(self.velocity)
        self.check_collision()
    def go_down(self):
        if(self.arena().check_arena_bounds(self) == 4): return
        super().setheading(270)
        super().forward(self.velocity)
        self.check_collision()
    def go_right(self):
        if(self.arena().check_arena_bounds(self) == 3): return
        super().setheading(0)
        super().forward(self.velocity)
        self.check_collision()
    #endregion---------------------------------------------------------------------------------------
        
    def lister_event(self):
        turtle.listen()
        turtle.onkeypress(self.go_forward, "w")
        turtle.onkeypress(self.go_down, "s")
        turtle.onkeypress(self.go_left, "a")
        turtle.onkeypress(self.go_right, "d")

    #Override
    def drawn(self):
        super().showturtle()

    #Check if is colliding and do something depending what is colliding.
    def check_collision(self):
        colliding_element = self.arena().check_collision(self.element_index_arena())

        if(type(colliding_element) != int):
            return

        if(type(self.arena().elements[colliding_element]) == Apple):
            self.apple_collision(self.arena().elements[colliding_element])

    #region Object collision--------------------------------------------------------------------------
    def apple_collision(self, apple: Apple):
        if(apple.apple_type is AppleType.BAD_APPLE):
            self.hp -= 1
            if(self.hp <= 0):
                turtle.bye()
        elif (apple.apple_type is AppleType.GOOD_APPLE):
            self.score += 1

        self.arena().show_player_info(self, Consts.arena_text_x, Consts.arena_text_y, Consts.arena_text_space_between)
        apple.randomize_location()