from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.goto (-40,200)
        self.update_score()

    def add_score_right(self):
        self.r_score+=1
        self.update_score()

    def add_score_left(self):
        self.l_score+=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}:{self.r_score}",align="center",font=("Courier",80,"normal"))