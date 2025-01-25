from turtle import *


class Scoreboard(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x_cor,y_cor)
        self.write(f"{self.score}", False, "center",("ubuntu",40,"bold"))
        self.hideturtle()

    def scoring(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "center", ("ubuntu", 40, "bold"))