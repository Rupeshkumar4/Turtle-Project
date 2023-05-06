from turtle import Turtle , Screen
import random
turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
"wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
turtle.pensize(4)
turtle.speed("fast")

for _ in range(200):
    turtle.pencolor(random.choice(colours)) 
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
turtle.penup()
turtle.home()
screen = Screen()

screen.exitonclick()