# to create the game the first i will have to:
#create the pingpong_paddle
#create the ball ,
#make the ball move when it hits raket
#create score list
#create middle line
#create screen
from ball import Ball

from turtle import Turtle,Screen
from paddle import Padle
import time
import time

screen=Screen()
screen.listen()
screen.setup(height=600,width=800)
screen.title("PingPong Game")
screen.bgcolor("black")
screen.tracer(0)

ball=Ball()

padle_right=Padle(350)
padle_left=Padle(-350)


screen.onkey(fun=padle_right.move_up,key="Up")
screen.onkey(fun=padle_right.move_down,key="Down")
screen.onkey(fun=padle_left.move_up,key="w")
screen.onkey(fun=padle_left.move_down,key="a")
game_is_on=True



while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()











screen.exitonclick()