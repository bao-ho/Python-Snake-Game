from turtle import Screen, Turtle
import time
from typing import overload
from snake import Snake
from food import Food
from text import Text

SPEED = 10
SNAKE_WIDTH = 20
FOOD_WIDTH = SNAKE_WIDTH*0.7
SCREEN_SIZE = 600
SCORE_TEXT_HEIGHT = 24
INSTRUCTION_TEXT_HEIGHT = 16
GAME_OVER_TEXT_HEIGHT = 30
POSSIBLE_RANGE = SCREEN_SIZE/2 - SNAKE_WIDTH


screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Feed your snake!")
screen.tracer(0)

game_paused = False

def play_or_pause():
    global game_paused
    game_paused = not game_paused 

game_on = True

def quit_game():
    global game_on
    game_on = False

game_restart  = False

def restart_game():
    global game_restart
    game_restart = True


screen.onkey(key='space', fun=play_or_pause)
screen.onkey(key='Escape', fun=quit_game)
screen.onkey(key='Return', fun=restart_game)
screen.listen()

fat_slob = Snake(width=SNAKE_WIDTH)
fast_food = Food(width=FOOD_WIDTH, possible_range=POSSIBLE_RANGE)
game_score = Text(x=0, y=SCREEN_SIZE/2-SCORE_TEXT_HEIGHT*2, text_height=SCORE_TEXT_HEIGHT, color='yellow')
instruction = Text(x=0, y=-SCREEN_SIZE/2+INSTRUCTION_TEXT_HEIGHT*1.5, text_height=INSTRUCTION_TEXT_HEIGHT, color='white')
game_over = Text(x=0, y=0, text_height=GAME_OVER_TEXT_HEIGHT, color='white')
instruction.update("Keys: 'SPACE' to pause/un-pause;    'ESCAPE' to quit;    'RETURN' to restart")

while game_on:
    if fat_slob.alive:
        screen.update()
        time.sleep(1/SPEED)
        if not game_paused:
            fat_slob.move()
            fat_slob.update(food=fast_food, possible_range=POSSIBLE_RANGE)
            game_score.update(f'Score: {fat_slob.length()}')
    else:
        if game_restart:
            fat_slob.restart()
            fast_food.update()
            fat_slob.alive = True
            game_restart = False
            game_over.update('')
        else:
            game_over.update('Game over !')


