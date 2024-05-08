import pgzrun
import random

WIDTH = 800
HEIGHT = 600
center_x = WIDTH/2
center_y = HEIGHT/2
center = (center_x,center_y)

current_level = 1
final_level = 6
gameover = False
gamecomplete = False
ITEMS = ["bag","battery","bottle","chips"]
items = []
animations = []

def draw():
    global items,current_level,gameover,gamecomplete
    screen.clear()
    screen.blit("bground",(0,0))
    if gameover:
        display_message("Game Over","Try again")
    elif gamecomplete:
        display_message("Congratulations!", "You beat the game!")
    else:
        for item in items:
            item.draw()

def update():
    global items,current_level
    if len(items) == 0:
        items = make_items(current_level)






pgzrun.go()