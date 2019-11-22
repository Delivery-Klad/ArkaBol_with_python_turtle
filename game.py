import turtle
from random import choice, randint

game = turtle.Screen()
game.title("game")
game.setup(width=1.0, height=1.0)
game.bgcolor("black")
game.tracer(1)

border = turtle.Turtle()
border.speed(0)
border.color("gray")

border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

heart1 = turtle.Turtle()
heart1.shape("circle")
heart1.color("red")
heart1.penup()
heart1.goto(-450, 280)

heart2 = turtle.Turtle()
heart2.shape("circle")
heart2.color("red")
heart2.penup()
heart2.goto(-400, 280)

heart3 = turtle.Turtle()
heart3.shape("circle")
heart3.color("red")
heart3.penup()
heart3.goto(-350, 280)

heart4 = turtle.Turtle()
heart4.shape("circle")
heart4.color("red")
heart4.penup()
heart4.goto(450, 280)

heart5 = turtle.Turtle()
heart5.shape("circle")
heart5.color("red")
heart5.penup()
heart5.goto(400, 280)

heart6 = turtle.Turtle()
heart6.shape("circle")
heart6.color("red")
heart6.penup()
heart6.goto(350, 280)

border.goto(0, 300)
border.color("black")
border.goto(0, -300)
border.hideturtle()

player_a = turtle.Turtle()
player_a.color("white")
player_a.shape("square")
player_a.shapesize(5, 1)
player_a.penup()
player_a.goto(-450, 0)

player_b = turtle.Turtle()
player_b.color("white")
player_b.shape("square")
player_b.shapesize(5, 1)
player_b.penup()
player_b.goto(450, 0)

ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("black")
ball.dx = choice([-4, -3, -2, 2, 3, 4])
ball.dy = choice([-4, -3, -2, 2, 3, 4])
ball.penup()

FONT = ("Arial", 44)
score_a = 0
score_b = 0

winner = turtle.Turtle(visible=False)
winner.color("white")
winner.penup()
winner.setposition(0, 0)
winner.write(score_a, font=FONT)
winner.clear()


def move_up_left():
    y = player_a.ycor()
    if y > 240:
        y = 240
    player_a.sety(y+10)


def move_down_left():
    y = player_a.ycor()
    if y < -240:
        y = -240
    player_a.sety(y-10)


def move_up_right():
    y = player_b.ycor()
    if y > 240:
        y = 240
    player_b.sety(y+10)


def move_down_right():
    y = player_b.ycor()
    if y < -240:
        y = -240
    player_b.sety(y-10)


game.listen()
game.onkeypress(move_up_left, "w")
game.onkeypress(move_down_left, "s")

game.onkeypress(move_up_right, "o")
game.onkeypress(move_down_right, "l")

while True:
    game.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >= 290:
        ball.dy = -ball.dy
    if ball.ycor() <= -290:
        ball.dy = -ball.dy
    if ball.xcor() >= 490:
        score_b -= -1
        if score_b == 1:
            heart6.color("gray")
        elif score_b == 2:
            heart5.color("gray")
        elif score_b == 3:
            heart4.color("gray")
            ball.color("gray")
            player_a.color("gray")
            player_b.color("gray")
            winner.write("player left win", font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    if ball.xcor() <= -490:
        score_a -= -1
        if score_a == 1:
            heart3.color("gray")
        elif score_a == 2:
            heart2.color("gray")
        elif score_a == 3:
            heart1.color("gray")
            ball.color("gray")
            player_a.color("gray")
            player_b.color("gray")
            winner.write("player right win", font=FONT)
        ball.goto(0, randint(-150, 1))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    if player_b.ycor()-50 <= ball.ycor() <= player_b.ycor()+50 \
            and player_b.xcor() - 5 <= ball.xcor() <= player_b.xcor() + 5:
        ball.dx = -ball.dx

    if player_a.ycor()-50 <= ball.ycor() <= player_a.ycor()+50 \
            and player_a.xcor() - 5 <= ball.xcor() <= player_a.xcor() + 5:
        ball.dx = -ball.dx

game.mainloop()

