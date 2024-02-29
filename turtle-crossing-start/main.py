import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    # Detect When car collides turtle
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect when turtle reached other end
    # if player.ycor() > 300:
    #     game_is_on = False
    if player.is_at_finish_line():
        player.go_to()
        car_manager.level_up()
        scoreboard.increase_level()




screen.exitonclick()