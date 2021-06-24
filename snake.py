from turtle import Turtle, Screen

SHAPE = "circle"
COLOR = "green"
BABY_LENGTH = 10
STAMP_SIZE = 20
FOOD_EATEN = True

class Snake:
    def __init__(self, width):
        self.segment_size = width
        self.relative_size = self.segment_size/STAMP_SIZE
        self.segments = []
        for i in range(BABY_LENGTH):
            self.add((-i*width,0))
        self.head = self.segments[0]

        def move_up():
            if self.head.heading() == 270:
                return
            self.head.setheading(90)

        def move_down():
            if self.head.heading() == 90:
                return
            self.head.setheading(270)

        def move_right():
            if self.head.heading() == 180:
                return
            self.head.setheading(0)

        def move_left():
            if self.head.heading() == 0:
                return
            self.head.setheading(180)
            

        self.alive = True
        self.screen = Screen()
        self.screen.onkey(key="Up", fun=move_up)    
        self.screen.onkey(key="Down", fun=move_down)    
        self.screen.onkey(key="Left", fun=move_left)    
        self.screen.onkey(key="Right", fun=move_right)    
        self.screen.listen()

    def add(self, position):
        self.relative_size = self.segment_size/STAMP_SIZE
        segment = Turtle(SHAPE)
        segment.color(COLOR)
        segment.penup()
        segment.goto(position)
        segment.shapesize(stretch_len=self.relative_size, stretch_wid=self.relative_size)
        self.segments.append(segment)
    
    def length(self):
        return len(self.segments)

    def restart(self):
        for segment in self.segments:
            segment.reset()
        self.segments = []
        for i in range(BABY_LENGTH):
            self.add((-i*self.segment_size,0))
        self.head = self.segments[0]
    
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
        self.head.forward(self.segment_size)

    def update(self, food, possible_range):
        if self.head.distance(food) < self.segment_size:
            self.add(self.segments[-1].position())
            food.update()
        
        if abs(self.head.position()[0]) > possible_range or abs(self.head.position()[1]) > possible_range:
            self.alive = False


        for segment in self.segments[1:]:
            if self.head.distance(segment) < self.segment_size/2:
                self.alive = False

    
    
