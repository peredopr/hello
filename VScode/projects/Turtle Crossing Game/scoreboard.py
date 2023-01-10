from player import Player

class Scoreboard(Player):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.pu()
        self.goto(-360, 260)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=("courier", 20, "normal"))


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("courier", 30, "normal"))
    

