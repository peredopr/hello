from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
text_input = screen.textinput(title="Make your bet!", prompt="Who will win this race? Select a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [100, 70, 40, 10, -20, -50]
turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.goto(x=-225, y=y_coordinates[index])
    new_turtle.color(colors[index])
    turtles.append(new_turtle)

race = True
while race:
    for turtle in turtles:
        if turtle.xcor() > 217:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == text_input:
                print(f"You've won! The {winning_color} turtle has won!")
            else:
                print(f"You've lost! The {winning_color} turtle has won!")
        steps = random.randint(0, 10)
        turtle.forward(steps)





screen.exitonclick()