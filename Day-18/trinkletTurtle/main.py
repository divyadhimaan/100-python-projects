# from turtle import Turtle, Screen
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

# colors = ["blue", "cyan", "chartreuse", "yellow", "dark orange", "red", "deep pink", "indigo"]
directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    return (r,g,b)

def draw_shape(sides):
    angle = 360/sides
    timmy.pensize(10)
    timmy.color(random_color())
    for i in range(0,sides):
        timmy.forward(100)
        timmy.right(angle)
        
        
def random_walk():
    timmy.pensize(10)
    timmy.speed("fastest")
    for i in range(0,500):
        current_direction = random.choice(directions)
        timmy.color(random_color())
        timmy.forward(50)
        timmy.setheading(current_direction)
    
def draw_spirograph(size_of_gap):
    timmy.speed("fastest")
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)
    
# for sides in range(3,11):
#     draw_shape(sides)

# random_walk()

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()