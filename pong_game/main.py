from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
SPEED = 0
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.pup, "Up")
screen.onkey(r_paddle.pdown, "Down")
screen.onkey(l_paddle.pup, "w")
screen.onkey(l_paddle.pdown, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50 or ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        ball.bounce_x()



    # Detect R_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # Detect L_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()











screen.exitonclick()
