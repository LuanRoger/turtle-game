from turtle import Turtle

class FontRenderer(Turtle):
    text: str
    x: int
    y: int

    def __init__(self, font, font_color: str, x: int, y: int) -> None:
        super().__init__(shape="arrow", undobuffersize=1, visible=False)
        super().penup()
        super().hideturtle()

        self.font = font
        self.font_color = font_color
        self.x = x
        self.y = y

    def set_text(self, text: str):
        self.text = text

    def drawn_text(self):
        super().undo()

        super().color(self.font_color)
        super().setpos(self.x, self.y)
        super().write(self.text, font=self.font)