import turtle
from arena import Arena
from cosnts import Consts
from player import Player
from apple import Apple, AppleType

#region Window---------------------------------------------------------------------------------------------
window = turtle.Screen()
window.title("Game of the year")
window.bgcolor("black")

#region Instanciations--------------------------------------------------------------------------------------
arena = Arena()
player = Player(x=0, y=0, arena=arena, shape="turtle")
god_apple = Apple(x=-100, y=100, arena = arena, color="red", type=AppleType.GOOD_APPLE)
bad_apple = Apple(x=100, y= 100, arena = arena, color="green", type=AppleType.BAD_APPLE)

#region Add elements to arena--------------------------------------------------------------------------------
arena.add_element(player)
arena.add_element(god_apple)
arena.add_element(bad_apple)

#region Drawn elements in arena-------------------------------------------------------------------------------
arena.drawn(-338, -275, (window.window_width() - 15, window.window_height() - 50), "snow3")
arena.drawn_elements()
arena.show_player_info(player, Consts.arena_text_x, Consts.arena_text_y, Consts.arena_text_space_between)

#region Player move and maniloop-------------------------------------------------------------------------------
player.lister_event()
window.mainloop()