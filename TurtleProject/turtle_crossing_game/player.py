from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle): # inherient from turtle class
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION) #initial make turtle at starting position
        self.setheading(90) # make turtle to face northward

        # Up movement function

    def go_up(self):
        self.forward(MOVE_DISTANCE)
    def go_down(self):
        self.backward(MOVE_DISTANCE)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
    

