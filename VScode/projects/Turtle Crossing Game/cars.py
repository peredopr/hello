from turtle import Turtle
import random

finish_value = 210
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
colors = ["orange", "red", "yellow", "blue", "green", "brown", "pink", "purple"]

class Cars():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_int = random.randint(1, 4)
        if random_int == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.pu()
            new_car.color(random.choice(colors))
            new_y = random.randint(-200, 200)
            new_car.goto(400, new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT