from turtle import *


class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.bar = []
        for gap in range(-280, 300, 40):
            a = Turtle()
            a.shape("square")
            a.shapesize(1,0.3)
            a.penup()
            a.color("white")
            a.goto(0, gap)
            self.bar.append(a)
