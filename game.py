import turtle
from random import choice, randint

# region blocks
hp1 = 3
hp2 = 3
hp3 = 3
hp4 = 3
hp5 = 3
hp6 = 3
hp7 = 3
hp8 = 3

a = True
b = True
c = True
d = True
e = True
f = True
g = True
h = True
# endregion
# region window
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


# endregion

# region hearts
def heart_builder(turtle2, x, y):
    turtle2.speed(0)
    turtle2.color("red")
    turtle2.penup()
    turtle2.goto(x, y)
    turtle2.pendown()
    turtle2.begin_fill()
    turtle2.goto(x - 10, y)
    turtle2.goto(x - 10, y - 5)
    turtle2.goto(x - 15, y - 5)
    turtle2.goto(x - 15, y - 10)
    turtle2.goto(x - 20, y - 10)
    turtle2.goto(x - 20, y - 5)
    turtle2.goto(x - 25, y - 5)
    turtle2.goto(x - 25, y)
    turtle2.goto(x - 35, y)
    turtle2.goto(x - 35, y - 5)
    turtle2.goto(x - 40, y - 5)
    turtle2.goto(x - 40, y - 15)
    turtle2.goto(x - 35, y - 15)
    turtle2.goto(x - 35, y - 20)
    turtle2.goto(x - 30, y - 20)
    turtle2.goto(x - 30, y - 25)
    turtle2.goto(x - 25, y - 25)
    turtle2.goto(x - 25, y - 30)
    turtle2.goto(x - 20, y - 30)
    turtle2.goto(x - 20, y - 35)
    turtle2.goto(x - 15, y - 35)
    turtle2.goto(x - 15, y - 30)
    turtle2.goto(x - 10, y - 30)
    turtle2.goto(x - 10, y - 25)
    turtle2.goto(x - 5, y - 25)
    turtle2.goto(x - 5, y - 20)
    turtle2.goto(x, y - 20)
    turtle2.goto(x, y - 15)
    turtle2.goto(x + 5, y - 15)
    turtle2.goto(x + 5, y - 5)
    turtle2.goto(x, y - 5)
    turtle2.end_fill()


heart1 = turtle.Turtle(visible=False)
heart_builder(heart1, -450, 280)
heart2 = turtle.Turtle(visible=False)
heart_builder(heart2, -400, 280)
heart3 = turtle.Turtle(visible=False)
heart_builder(heart3, -350, 280)
heart4 = turtle.Turtle(visible=False)
heart_builder(heart4, 490, 280)
heart5 = turtle.Turtle(visible=False)
heart_builder(heart5, 440, 280)
heart6 = turtle.Turtle(visible=False)
heart_builder(heart6, 390, 280)

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
# endregion

# region balls
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.color("black")
ball.goto(-400, 0)
ball.dx = choice([-4, -3, -2, 2, 3, 4])
ball.dy = choice([-4, -3, -2, 2, 3, 4])

ball2 = turtle.Turtle()
ball2.shape("circle")
ball2.speed(0)
ball2.penup()
ball2.color("black")
ball2.goto(400, 0)
ball2.dx = choice([-4, -3, -2, 2, 3, 4])
ball2.dy = choice([-4, -3, -2, 2, 3, 4])

# endregion

# region winner text
FONT = ("Arial", 44)
score_a = 0
score_b = 0

winner = turtle.Turtle(visible=False)
winner.color("white")
winner.penup()
winner.setposition(0, 0)
winner.write(score_a, font=FONT)
winner.clear()


# endregion

# region button func
def move_up_left():
    y = player_a.ycor()
    if y > 240:
        y = 240
    player_a.sety(y + 10)


def move_down_left():
    y = player_a.ycor()
    if y < -240:
        y = -240
    player_a.sety(y - 10)


def move_up_right():
    y = player_b.ycor()
    if y > 240:
        y = 240
    player_b.sety(y + 10)


def move_down_right():
    y = player_b.ycor()
    if y < -240:
        y = -240
    player_b.sety(y - 10)


# endregion

# region big blocks
block_a = turtle.Turtle()
block_a.color("white")
block_a.speed(0)
block_a.shape("square")
block_a.shapesize(10, 5)
block_a.penup()
block_a.goto(0, 200)

block_b = turtle.Turtle()
block_b.color("white")
block_b.speed(0)
block_b.shape("square")
block_b.shapesize(10, 5)
block_b.penup()
block_b.goto(0, -200)

block_c = turtle.Turtle()
block_c.color("white")
block_c.speed(0)
block_c.shape("square")
block_c.shapesize(5, 10)
block_c.penup()
block_c.goto(0, 0)
# endregion

# region small blocks
block_d = turtle.Turtle()
block_d.color("white")
block_d.speed(0)
block_d.shape("square")
block_d.shapesize(4, 2)
block_d.penup()
block_d.goto(150, 60)

block_e = turtle.Turtle()
block_e.color("white")
block_e.speed(0)
block_e.shape("square")
block_e.shapesize(4, 2)
block_e.penup()
block_e.goto(-150, 60)

block_f = turtle.Turtle()
block_f.color("white")
block_f.speed(0)
block_f.shape("square")
block_f.shapesize(4, 2)
block_f.penup()
block_f.goto(-150, -60)

block_g = turtle.Turtle()
block_g.color("white")
block_g.speed(0)
block_g.shape("square")
block_g.shapesize(4, 2)
block_g.penup()
block_g.goto(150, -60)
# endregion

# region buttons
game.listen()
game.onkeypress(move_up_left, "w")
game.onkeypress(move_down_left, "s")

game.onkeypress(move_up_right, "o")
game.onkeypress(move_down_right, "l")
# endregion

while True:
    game.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)
    # region ball
    if ball.ycor() >= 290:
        ball.dy = -ball.dy
    if ball.ycor() <= -290:
        ball.dy = -ball.dy
    if ball.xcor() >= 490:
        score_b -= -1
        if score_b == 1:
            heart6.clear()
        elif score_b == 2:
            heart5.clear()
        elif score_b == 3:
            heart4.clear()
            ball.color("gray")
            ball2.color("gray")
            player_a.color("gray")
            player_b.color("gray")
            winner.penup()
            winner.goto(-500, 0)
            winner.write("player left win", font=FONT)
        ball.goto(-400, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    if ball.xcor() <= -490:
        score_a -= -1
        if score_a == 1:
            heart3.clear()
        elif score_a == 2:
            heart2.clear()
        elif score_a == 3:
            heart1.clear()
            ball.color("gray")
            ball2.color("gray")
            player_a.color("gray")
            player_b.color("gray")
            winner.penup()
            winner.goto(0, 0)
            winner.write("player right win", font=FONT)
        ball.goto(-400, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    # endregion
    # region ball2
    if ball2.ycor() >= 290:
        ball2.dy = -ball2.dy
    if ball2.ycor() <= -290:
        ball2.dy = -ball2.dy
    if ball2.xcor() >= 490:
        score_b -= -1
        if score_b == 1:
            heart6.clear()
        elif score_b == 2:
            heart5.clear()
        elif score_b == 3:
            heart4.clear()
            ball.color("gray")
            ball2.color("gray")
            player_a.color("gray")
            player_b.color("gray")
            winner.write("player left win", font=FONT)
        ball2.goto(400, 0)
        ball2.dx = choice([-4, -3, -2, 2, 3, 4])
        ball2.dy = choice([-4, -3, -2, 2, 3, 4])
    if ball2.xcor() <= -490:
        score_a -= -1
        if score_a == 1:
            heart3.clear()
        elif score_a == 2:
            heart2.clear()
        elif score_a == 3:
            heart1.clear()
            ball.color("gray")
            ball2.color("gray")
            player_a.color("gray")
            player_b.color("gray")
            winner.write("player right win", font=FONT)
        ball2.goto(400, 0)
        ball2.dx = choice([-4, -3, -2, 2, 3, 4])
        ball2.dy = choice([-4, -3, -2, 2, 3, 4])
    # endregion

    # region beat off
    if player_b.ycor() - 60 <= ball.ycor() <= player_b.ycor() + 60 \
            and player_b.xcor() - 20 <= ball.xcor() <= player_b.xcor() + 20:
        ball.dx = -ball.dx

    if player_a.ycor() - 60 <= ball.ycor() <= player_a.ycor() + 60 \
            and player_a.xcor() - 20 <= ball.xcor() <= player_a.xcor() + 20:
        ball.dx = -ball.dx

    if player_b.ycor() - 50 <= ball2.ycor() <= player_b.ycor() + 50 \
            and player_b.xcor() - 20 <= ball2.xcor() <= player_b.xcor() + 20:
        ball2.dx = -ball2.dx

    if player_a.ycor() - 50 <= ball2.ycor() <= player_a.ycor() + 50 \
            and player_a.xcor() - 20 <= ball2.xcor() <= player_a.xcor() + 20:
        ball2.dx = -ball2.dx
    if a:
        if block_a.ycor() - 120 <= ball2.ycor() <= block_a.ycor() + 120 \
                and block_a.xcor() - 60 <= ball2.xcor() <= block_a.xcor() + 60:
            ball2.dx = -ball2.dx
            hp1 += -1
            print(hp1)
    if b:
        if block_b.ycor() - 120 <= ball2.ycor() <= block_b.ycor() + 120 \
                and block_b.xcor() - 60 <= ball2.xcor() <= block_b.xcor() + 60:
            ball2.dx = -ball2.dx
            hp2 += -1
            print(hp2)
    if c:
        if block_c.ycor() - 50 <= ball2.ycor() <= block_c.ycor() + 50 \
                and block_c.xcor() - 110 <= ball2.xcor() <= block_c.xcor() + 110:
            ball2.dx = -ball2.dx
            hp3 += -1
            print(hp3)
    if d:
        if block_d.ycor() - 70 <= ball2.ycor() <= block_d.ycor() + 70 \
                and block_d.xcor() - 35 <= ball2.xcor() <= block_d.xcor() + 35:
            ball2.dx = -ball2.dx
            hp4 += -1
            print(hp4)
    if e:
        if block_e.ycor() - 70 <= ball2.ycor() <= block_e.ycor() + 70 \
                and block_e.xcor() - 35 <= ball2.xcor() <= block_e.xcor() + 35:
            ball2.dx = -ball2.dx
            hp5 += -1
            print(hp5)
    if f:
        if block_f.ycor() - 70 <= ball2.ycor() <= block_f.ycor() + 70 \
                and block_f.xcor() - 35 <= ball2.xcor() <= block_f.xcor() + 35:
            ball2.dx = -ball2.dx
            hp6 += -1
            print(hp6)
    if g:
        if block_g.ycor() - 70 <= ball2.ycor() <= block_g.ycor() + 70 \
                and block_g.xcor() - 35 <= ball2.xcor() <= block_g.xcor() + 35:
            ball2.dx = -ball2.dx
            hp7 += -1
            print(hp7)

    if a:
        if block_a.ycor() - 120 <= ball.ycor() <= block_a.ycor() + 120 \
                and block_a.xcor() - 60 <= ball.xcor() <= block_a.xcor() + 60:
            ball.dx = -ball.dx
            hp1 += -1
            print(hp1)
    if b:
        if block_b.ycor() - 120 <= ball.ycor() <= block_b.ycor() + 120 \
                and block_b.xcor() - 60 <= ball.xcor() <= block_b.xcor() + 60:
            ball.dx = -ball.dx
            hp2 += -1
            print(hp2)
    if c:
        if block_c.ycor() - 50 <= ball.ycor() <= block_c.ycor() + 50 \
                and block_c.xcor() - 110 <= ball.xcor() <= block_c.xcor() + 110:
            ball.dx = -ball.dx
            hp3 += -1
            print(hp3)
    if d:
        if block_d.ycor() - 70 <= ball.ycor() <= block_d.ycor() + 70 \
                and block_d.xcor() - 35 <= ball.xcor() <= block_d.xcor() + 35:
            ball.dx = -ball.dx
            hp4 += -1
            print(hp4)
    if e:
        if block_e.ycor() - 70 <= ball.ycor() <= block_e.ycor() + 70 \
                and block_e.xcor() - 35 <= ball.xcor() <= block_e.xcor() + 35:
            ball.dx = -ball.dx
            hp5 += -1
            print(hp5)
    if f:
        if block_f.ycor() - 70 <= ball.ycor() <= block_f.ycor() + 70 \
                and block_f.xcor() - 35 <= ball.xcor() <= block_f.xcor() + 35:
            ball.dx = -ball.dx
            hp6 += -1
            print(hp6)
    if g:
        if block_g.ycor() - 70 <= ball.ycor() <= block_g.ycor() + 70 \
                and block_g.xcor() - 35 <= ball.xcor() <= block_g.xcor() + 35:
            ball.dx = -ball.dx
            hp7 += -1
            print(hp7)
    if a:
        if hp1 == 0:
            block_a.reset()
            a = False
            block_a.speed(0)
            block_a.goto(0, 350)
    if b:
        if hp2 == 0:
            block_b.reset()
            b = False
            block_b.speed(0)
            block_b.goto(0, 350)
    if c:
        if hp3 == 0:
            block_c.reset()
            c = False
            block_c.speed(0)
            block_c.goto(0, 350)
    if d:
        if hp4 == 0:
            block_d.color("black")
            d = False
            block_d.speed(0)
            block_d.goto(0, 350)
    if e:
        if hp5 == 0:
            block_e.color("black")
            e = False
            block_e.speed(0)
            block_e.goto(0, 350)
    if f:
        if hp6 == 0:
            block_f.color("black")
            f = False
            block_f.speed(0)
            block_f.goto(0, 350)
    if g:
        if hp7 == 0:
            block_g.color("black")
            g = False
            block_g.speed(0)
            block_g.goto(0, 350)
    # endregion

game.mainloop()
