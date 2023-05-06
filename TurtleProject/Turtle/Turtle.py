from turtle import Turtle , Screen
import random

my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("green","red")
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)

# for i in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)

# for i in range(40):
#     my_turtle.pendown()
#     my_turtle.forward(3)
#     my_turtle.penup()
#     my_turtle.forward(3)    

    # my_turtle.left(90)

# for i in range(noOfSides):
#     angle = 360/noOfSides
    # for _ in range(i):
    #     my_turtle.forward(100)
    #     my_turtle.right(angle)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
"wheat", "SlateGray", "SeaGreen"]

def DrawShape(side):
    angle = 360/noOfSides

    for _ in range(noOfSides):
        my_turtle.fillcolor("violet")
        my_turtle.forward(100)
        my_turtle.right(angle)

def DrawShapes(side):
    angle = 360/noOfSides
    for _ in range(noOfSides):
        my_turtle.forward(100)
        my_turtle.left(angle)

for noOfSides in range(3,11):
    my_turtle.pencolor(random.choice(colours))
    DrawShape(noOfSides)
    DrawShapes(noOfSides)
    









screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())