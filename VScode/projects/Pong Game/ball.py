from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.0025
    

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    
    def bounce(self):
        self.y_move *= -1


    def p_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

        
    def reset_position(self):
        self.goto(0, 0)
        self.p_bounce()
        self.move_speed = 0.0025