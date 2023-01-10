from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
cars = Cars()
    

screen.listen()
screen.onkey(turtle.go_up, "w")



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    if turtle.finish_line():
        turtle.go_to_start()
        cars.increase_speed()
        scoreboard.increase_level()
    for car in cars.all_cars:
        if car.distance(turtle) < 25:
            game_on = False
            scoreboard.game_over()

    














screen.exitonclick()