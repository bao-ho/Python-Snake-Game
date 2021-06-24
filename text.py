from turtle import Turtle

class Text(Turtle):
    def __init__(self, x, y, text_height, color):
        super().__init__()
        self.text_height = text_height
        self.goto(x, y)
        self.color(color)
        self.hideturtle()
    
    def update(self, content):
        self.clear()
        self.write(content, move=False, align='center', font=("Arial", self.text_height, "normal"))
