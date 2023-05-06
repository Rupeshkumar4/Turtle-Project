from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        # roll a dice when we get 1 the we create a new car but it drawn dice ever 0.1s
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250) # specifing the range of car movement in y direction
            new_car.goto(300,random_y) # placing the car movement at right of x axis bt in range of y axis
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            # car.backward(STARTING_MOVE_DISTANCE)
            car.backward(self.car_speed)
            # moving car from right to left

    def level_up(self):
        self.car_speed += MOVE_INCREMENT 