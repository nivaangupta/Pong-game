from turtle import Turtle


class Ball(Turtle):
    def __init__(self, angle):
        super().__init__()
        self.shape("circle")
        self.shapesize(.75, .75)
        self.color("white")
        self.angle = angle
        self.setheading(self.angle)
        self.penup()
        self.num = 1
        self.speed(self.num)
        self.p1_miss = 0
        self.p2_miss = 0

    def keep_score(self):
        if self.xcor() < -500:
            self.p1_miss += 1
            self.goto(0, 0)
            self.setheading(self.heading()+180)
            return True
        elif self.xcor() > 500:
            self.p2_miss += 1
            self.goto(0, 0)
            self.setheading(self.heading() + 180)
            return True
        else:
            return False


