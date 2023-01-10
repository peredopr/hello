import turtle
import random


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pen_color = (r, g, b)
    return pen_color


tim = turtle.Turtle()
tim.shape("turtle")
turtle.colormode(255)
tim.speed("fastest")

def draw_circle(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)

draw_circle(2)

screen = turtle.Screen()
screen.exitonclick()
