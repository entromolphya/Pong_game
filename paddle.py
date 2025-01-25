from turtle import *


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_cor, 0)

    def up1(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 65
            self.goto(-350, new_y)
        else:
            return

    def down1(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 65
            self.goto(-350, new_y)
        else:
            return

    def up2(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 65
            self.goto(350, new_y)
        else:
            return

    def down2(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 65
            self.goto(350, new_y)
        else:
            return

    def move(self, x):
        listen()
        if x == 1:
            onkey(self.up1, "w")
            onkey(self.down1, "s")
        else:
            onkey(self.up2, "Up")
            onkey(self.down2, "Down")
