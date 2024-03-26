import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    carManager.create_car()
    carManager.move_cars()
    
    # turtle collides with car
    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    # detect turtle reaches goal
    if player.at_finish_line():
        player.go_to_start()
        carManager.level_up()
        scoreboard.level_up()
               
screen.exitonclick()