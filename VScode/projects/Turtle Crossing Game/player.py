from turtle import Turtle

STARTING_POSITION = (0, -270)
PASSES = 10
FINISH_Y = 210

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("turtle")
        self.pu()
        self.go_to_start()
        self.left(90)

    
    def go_up(self):
        self.forward(PASSES)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_Y:
            return True
        else:
            return False