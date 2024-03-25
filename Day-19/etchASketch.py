from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def rotate_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def rotate_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()