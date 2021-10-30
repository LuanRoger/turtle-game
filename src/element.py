from turtle import Turtle

# The element know where arena he is and can modify your oworn state but never
# from others elements. He can call functions from others elements 
class Element(Turtle):
    def arena(self):
        return self._arena
    
    def element_index_arena(self):
        return self._arena.get_element_index(self)

    def __init__(self, x: int, y: int, arena, shape: str = "arrow", color : str = "white"):
        super().__init__(shape=shape, undobuffersize=1, visible=False)
        super().penup()
        super().hideturtle()
        super().color(color)

        self._arena = arena
        super().setpos(x, y)
        
    #Virtual
    def drawn(self):
        pass