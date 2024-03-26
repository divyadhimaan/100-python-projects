from turtle import Turtle, Screen

DIRECTIONS = [0,90,180,270]

class Boundary(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270,-270)
        self.color("white")
        self.hideturtle()
        self.draw_boundary()
        
    def draw_boundary(self):
        self.setheading(DIRECTIONS[0])
        self.pendown()
        for i in range(4):
            self.forward(540)
            if i != 3:
                self.setheading(DIRECTIONS[i+1])

        
        
    
        