from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from boundary import Boundary
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

boundary = Boundary()

# creating snake and food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# continue_playing = True

# while continue_playing:
    
# Moving Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        
    # detect collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if (x_cor > 270 or x_cor < -270) or (y_cor > 270 or y_cor < -270):
        game_is_on = False
        scoreboard.game_over()
        
    # detect collision with tail - head collides with any segment in tail
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                    
    # time.sleep(10)
    # user_input_to_play = screen.textinput(title="Snake Game", prompt="Do you want to continue playing? Type y/n: ")
    # if user_input_to_play == 'n':
    #     continue_playing = False
    # elif user_input_to_play == 'y':
    #     scoreboard.reset()
    #     snake.reset()
    
screen.exitonclick()