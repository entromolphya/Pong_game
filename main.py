from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from bar import Bar

bgcolor("black")
setup(800, 600)
title("Pong")
color("green")
penup()
hideturtle()
tracer(0)

bar = Bar()
l_pad = Paddle(-350)
r_pad = Paddle(350)
ball = Ball()
scoreboard_l = Scoreboard(-280, 230)
scoreboard_r = Scoreboard(280, 230)

while True:
    update()
    time.sleep(0.07)
    l_pad.move(1)
    r_pad.move(2)
    ball.ball_move()
    if ball.ycor() > 278 or ball.ycor() < -278:
        ball.bounce_y()

    if r_pad.distance(ball) < 55 and ball.xcor() < 340 or l_pad.distance(ball) < 55 and ball.xcor() > -340:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_pos()
        scoreboard_l.scoring()

    if ball.xcor() < -390:
        ball.reset_pos()
        scoreboard_r.scoring()

    if scoreboard_r.score >= 2 or scoreboard_l.score >= 2:
        if scoreboard_r.score == 2:
            write(f"Game Over!\nThe Player R wins", False, "center", ("ubuntu", 20, "bold"))
        else:
            write(f"Game Over!\nThe Player L wins", False, "center", ("ubuntu", 20, "bold"))
        break

exitonclick()
