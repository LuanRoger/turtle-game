from turtle import Turtle
from typing import List, Tuple
from element import Element
from font_renderer import FontRenderer

class Arena:
    arena_renderer: Turtle

    font = ("Arial", 18, 'bold')
    font_color = "white"

    texts = [] #List<FontRenderer>
    elements = [] #List<Element>
    arena_limit_vertex: List #List<Tuple>

    def __init__(self):
        self.arena_renderer = Turtle(shape = "arrow", visible = False)
        self.arena_renderer.penup()

    #region Manage elements-------------------------------------------------------------------
    def add_element(self, element: Element):
        self.elements.append(element)

    def remove_element(self, element: Element):
        self.elements.remove(element)

    def get_element_index(self, element: Element) -> int:
        return self.elements.index(element)

    #region Drawn arena and elements-----------------------------------------------------------
    def drawn(self, x: int, y: int, side_size: Tuple, color: str = "red", size = 5):
        self.arena_limit_vertex = []
        self.arena_renderer.setpos(x, y)
        self.arena_renderer.color(color)
        self.arena_renderer.pendown()
        self.arena_renderer.pensize(size)

        #Diagonal vertex
        self.arena_limit_vertex.append((self.arena_renderer.xcor(), self.arena_renderer.ycor()))
        self.arena_renderer.setheading(0)
        self.arena_renderer.forward(side_size[0])
        self.arena_renderer.left(90)
        self.arena_renderer.forward(side_size[1])
        #Before return get the max vertex limit - Diagonal vertex
        self.arena_limit_vertex.append((self.arena_renderer.xcor(), self.arena_renderer.ycor()))
        self.arena_renderer.left(90)
        self.arena_renderer.forward(side_size[0])
        self.arena_renderer.left(90)
        self.arena_renderer.forward(side_size[1])

        print(self.arena_limit_vertex)

        self.arena_renderer.penup()

    def drawn_elements(self):
        for element in self.elements:
            element.drawn()
    #endregion
    
    def show_player_info(self, player, x: int, y: int, space_between_info: int):
        if(len(self.texts) < 2):
            self.texts.append(FontRenderer(self.font, self.font_color, x, y))
            self.texts.append(FontRenderer(self.font, self.font_color, x + space_between_info, y))
        
        self.texts[0].undo()
        self.texts[1].undo()

        self.texts[0].set_text(f"HP: {player.hp}")
        self.texts[1].set_text(f"Pontos: {player.score}")

        self.texts[0].drawn_text()
        self.texts[1].drawn_text()

    #region Collision-----------------------------------------------------------------------------
    def check_collision(self, element_checker_index: int) -> int: #ElementIndex
        elements_to_search = self.elements.copy()
        elements_to_search.pop(element_checker_index)

        for element in elements_to_search:
            distance = self.elements[element_checker_index].distance(element.pos())
            if(distance < 30):
                return self.elements.index(element)
    
    def check_arena_bounds(self, element: Element) -> int:
        # 0 - Non-Colliding
        # 1 - Left
        # 2 - Top
        # 3 - Right
        # 4 - Bottom
        tolerance = 23
        if(element.xcor() <= self.arena_limit_vertex[0][0] + tolerance):
            return 1
        if(element.ycor() >= self.arena_limit_vertex[1][1] - tolerance):
            return 2
        if(element.xcor() >= self.arena_limit_vertex[1][0] - tolerance):
            return 3
        if(element.ycor() <= self.arena_limit_vertex[0][1] + tolerance):
            return 4
        
        return 0