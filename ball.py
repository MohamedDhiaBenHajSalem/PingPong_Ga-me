from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)



    def move_ball(self):
        self.goto(self.xcor()+10,self.ycor()+10)


