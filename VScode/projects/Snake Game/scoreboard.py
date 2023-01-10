from turtle import Turtle
ALIGN ="center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 260)
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
