from turtle import Turtle


class Player:
    def __init__(self, player_number):
        self.yax = 0
        self.blocks = []
        self.create_player(player_number)

    def create_player(self, player_num):
        for _ in range(5):
            self.player = Turtle(shape="square")
            self.player.speed("fastest")
            self.player.penup()
            self.player.color("white")
            if player_num == 1:
                self.player.goto(-475, self.yax)
            elif player_num == 2:
                self.player.goto(475, self.yax)
            self.yax += 20
            self.blocks.append(self.player)

    def up1(self):
        for block in self.blocks:
            block.setheading(90)
            block.forward(40)

    def down1(self):
        for block in self.blocks:
            block.setheading(270)
            block.forward(40)

    def up2(self):
        for block in self.blocks:
            block.setheading(90)
            block.forward(40)

    def down2(self):
        for block in self.blocks:
            block.setheading(270)
            block.forward(40)

# What I could have done:
# 1. I could have just made 1 turtle and adjust its shape and size rather than stacking multiple turtles, this will
# provide the necessary sophistication in angle change of the ball





