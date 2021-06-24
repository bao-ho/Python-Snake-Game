import random
from turtle import Turtle


STAMP_SIZE = 20

class Food(Turtle):
    def __init__(self, width, possible_range):
        super().__init__()
        range = possible_range
        x = random.randint(-range, range)
        y = random.randint(-range, range)
        self.shape("square")
        self.penup()
        self.goto(x,y)
        self.color("red")
        r = width/STAMP_SIZE
        self.shapesize(stretch_wid=r, stretch_len=r)
        self.range = range

    def update(self):
        range = self.range
        x = random.randint(-range, range)
        y = random.randint(-range, range)
        self.goto(x,y)    