from turtle import Turtle


class Score(Turtle):
    def __init__(self, num):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.location(num)

    def display_score(self, num):
        self.clear()
        self.write(f"{num}", False, align="center", font=('courier', 84, 'normal'))

    def location(self, num):
        if num == 2:
            self.goto(100, 150)
        if num == 1:
            self.goto(-100, 150)

    def display_winner(self, num):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!\nPlayer {num} WON", False, align="center", font=('courier', 84, 'normal'))
