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
from  score_board import Score_Board

screen=Screen()
screen.listen()
screen.setup(height=600,width=800)
screen.title("PingPong Game")
screen.bgcolor("black")
screen.tracer(0)

ball=Ball()
score=Score_Board()

padle_right=Padle(350)
padle_left=Padle(-350)


screen.onkey(fun=padle_right.move_up,key="Up")
screen.onkey(fun=padle_right.move_down,key="Down")
screen.onkey(fun=padle_left.move_up,key="w")
screen.onkey(fun=padle_left.move_down,key="a")
game_is_on=True



while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(padle_right)<50 and ball.xcor()>320 or ball.distance(padle_left)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.distance (padle_right)>50 and ball.xcor()>380  :
        ball.reset_ball()
        ball.bounce_x()
        score.add_score_left()

    if ball.distance(padle_left)>50 and ball.xcor()<-380:
        ball.reset_ball()
        ball.bounce_x()
        score.add_score_right()


    if score.r_score ==10 :
        game_is_on=False


    if  score.l_score==10 :
        game_is_on=False









screen.exitonclick()