import turtle
import random
from main import color_list

turtle.colormode(255)
john = turtle.Turtle()

john.hideturtle()
john.setheading(225)
john.pu()
john.forward(350)
john.setheading(0)
john.speed("fastest")
x = 1
while x <= 11:
    for line in range(11):
        john.pu()
        john.dot(20, random.choice(color_list))
        john.forward(50)
    john.setheading(90)
    john.forward(50)
    john.setheading(180)
    john.forward(550)
    john.setheading(0)
    x += 1













screen = turtle.Screen()
screen = screen.exitonclick()