
from turtle import Turtle

class Padle(Turtle):
    def __init__(self,position1):
        super().__init__()
        self.position1=position1
        self.shape("square")
        self.penup()
        self.setpos(self.position1, 0)
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.color("white")

    def move_up(self):
        if 340 > self.ycor():
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -340:
            self.sety(self.ycor() - 20)
