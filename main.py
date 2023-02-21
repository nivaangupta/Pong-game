from turtle import Screen, Turtle
from players import Player
from ball import Ball
from scoreboard import Score

game_is_on = True
angle = 135
speed = 3
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

outline = Turtle(shape="square")
outline.color("white")
outline.shapesize(4, 4)
outline.hideturtle()
outline.penup()
outline.goto(0, 300)
for _ in range(30):
    outline.setheading(270)
    outline.pendown()
    outline.forward(10)
    outline.penup()
    outline.forward(10)
screen.update()


player1 = Player(1)
p1 = Score(1)
player2 = Player(2)
p2 = Score(2)
ball = Ball(angle)
p1.display_score(ball.p2_miss)
p2.display_score(ball.p1_miss)
screen.update()

while game_is_on:
    screen.update()
    # player controlling the bars
    screen.onkey(player1.up1, "w")
    screen.onkey(player1.down1, "z")
    screen.onkey(player2.up2, "u")
    screen.onkey(player2.down2, "n")
    # ball's motion
    ball.forward(speed)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.setheading(ball.heading() + 90)

    for block in player1.blocks:
        if block.distance(ball) < 20:
            ball.setheading(ball.heading() + 90)
            speed += 0.2

    for block in player2.blocks:
        if block.distance(ball) < 20:
            ball.setheading(ball.heading() + 90)
            speed += 0.2

    if ball.keep_score():
        p1.display_score(ball.p2_miss)
        p2.display_score(ball.p1_miss)
        speed = 3

    if ball.p2_miss >= 5:
        p1.display_winner(1)
        p2.clear()
        game_is_on = False
    elif ball.p1_miss >= 5:
        p2.display_winner(2)
        p1.clear()
        game_is_on = False

screen.exitonclick()

# while using the tracer method it is mandatory to use while loop to keep updating to show the desired animation
