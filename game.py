import turtle
from random import choice

# region blocks
block_a = turtle.Turtle()
block_b = turtle.Turtle()
block_c = turtle.Turtle()
block_d = turtle.Turtle()
block_e = turtle.Turtle()
block_f = turtle.Turtle()
block_g = turtle.Turtle()
block_h = turtle.Turtle()
blocks = [block_a, block_b, block_c, block_d, block_e, block_f, block_g, block_h]
HP = [3, 3, 3, 3, 3, 3, 3, 0]
destroys = [True, True, True, True, True, True, True, True]
noBlocks = False
rev_block1 = True
rev_block2 = True
global_x = -400
# endregion
# region window
game = turtle.Screen()
game.title("ArkaBol")
game.setup(width=1.0, height=1.0)
game.bgcolor("black")
game.tracer(1)

zone = turtle.Turtle()
zone.speed(0)
zone.color("gray")
zone.begin_fill()
zone.goto(-500, 300)
zone.goto(500, 300)
zone.goto(500, -300)
zone.goto(-500, -300)
zone.goto(-500, 300)
zone.end_fill()
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

zone.goto(0, 300)
zone.color("gray")
zone.goto(0, -300)
zone.hideturtle()
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
winner.setposition(-250, 0)
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

# region blocks
for i in range(len(blocks) - 1):
    blocks[i].color("white")
    blocks[i].speed(0)
    blocks[i].shape("square")
blocks[0].shapesize(10, 5)
blocks[0].penup()
blocks[0].goto(0, 200)

blocks[1].shapesize(10, 5)
blocks[1].penup()
blocks[1].goto(0, -200)

blocks[2].shapesize(5, 10)
blocks[2].penup()
blocks[2].goto(0, 0)

blocks[3].shapesize(4, 2)
blocks[3].penup()
blocks[3].goto(150, 60)

blocks[4].shapesize(4, 2)
blocks[4].penup()
blocks[4].goto(-150, 60)

blocks[5].shapesize(4, 2)
blocks[5].penup()
blocks[5].goto(-150, -60)

blocks[6].shapesize(4, 2)
blocks[6].penup()
blocks[6].goto(150, -60)
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
    if ball2.ycor() + 20 >= ball.ycor() >= ball2.ycor() - 20 and ball2.xcor() + 20 >= ball.xcor() >= ball2.xcor() - 20:
        if rev_block1:
            ball.dx = -ball.dx
            rev_block1 = False
    if ball.ycor() >= 290:
        rev_block1 = True
        ball.dy = -ball.dy
    if ball.ycor() <= -290:
        rev_block1 = True
        ball.dy = -ball.dy
    if ball.xcor() >= 490:
        rev_block1 = True
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
        ball.goto(0, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    if ball.xcor() <= -490:
        rev_block1 = True
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
        ball.goto(0, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    # endregion
    # region ball2
    if ball.ycor() + 20 >= ball2.ycor() >= ball.ycor() - 20 and ball.xcor() + 20 >= ball2.xcor() >= ball.xcor() - 20:
        if rev_block2:
            ball2.dx = -ball2.dx
            rev_block2 = False
    if ball2.ycor() >= 290:
        rev_block2 = True
        ball2.dy = -ball2.dy
    if ball2.ycor() <= -290:
        rev_block2 = True
        ball2.dy = -ball2.dy
    if ball2.xcor() >= 490:
        rev_block2 = True
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
        ball2.goto(0, 0)
        ball2.dx = choice([-4, -3, -2, 2, 3, 4])
        ball2.dy = choice([-4, -3, -2, 2, 3, 4])
    if ball2.xcor() <= -490:
        rev_block2 = True
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
        ball2.goto(0, 0)
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
    # endregion

    # region hp
    if destroys[0]:
        if block_a.ycor() - 120 <= ball2.ycor() <= block_a.ycor() + 120 \
                and block_a.xcor() - 60 <= ball2.xcor() <= block_a.xcor() + 60:
            ball2.dx = -ball2.dx
            HP[0] += -1
            print(HP[0], noBlocks)
    if destroys[1]:
        if block_b.ycor() - 120 <= ball2.ycor() <= block_b.ycor() + 120 \
                and block_b.xcor() - 60 <= ball2.xcor() <= block_b.xcor() + 60:
            ball2.dx = -ball2.dx
            HP[1] += -1
            print(HP[1], noBlocks)
    if destroys[2]:
        if block_c.ycor() - 50 <= ball2.ycor() <= block_c.ycor() + 50 \
                and block_c.xcor() - 110 <= ball2.xcor() <= block_c.xcor() + 110:
            ball2.dx = -ball2.dx
            HP[2] += -1
            print(HP[2], noBlocks)
    if destroys[3]:
        if block_d.ycor() - 70 <= ball2.ycor() <= block_d.ycor() + 70 \
                and block_d.xcor() - 35 <= ball2.xcor() <= block_d.xcor() + 35:
            ball2.dx = -ball2.dx
            HP[3] += -1
            print(HP[3], noBlocks)
    if destroys[4]:
        if block_e.ycor() - 70 <= ball2.ycor() <= block_e.ycor() + 70 \
                and block_e.xcor() - 35 <= ball2.xcor() <= block_e.xcor() + 35:
            ball2.dx = -ball2.dx
            HP[4] += -1
            print(HP[4], noBlocks)
    if destroys[5]:
        if block_f.ycor() - 70 <= ball2.ycor() <= block_f.ycor() + 70 \
                and block_f.xcor() - 35 <= ball2.xcor() <= block_f.xcor() + 35:
            ball2.dx = -ball2.dx
            HP[5] += -1
            print(HP[5], noBlocks)
    if destroys[6]:
        if block_g.ycor() - 70 <= ball2.ycor() <= block_g.ycor() + 70 \
                and block_g.xcor() - 35 <= ball2.xcor() <= block_g.xcor() + 35:
            ball2.dx = -ball2.dx
            HP[6] += -1
            print(HP[6], noBlocks)
    if destroys[0]:
        if block_a.ycor() - 120 <= ball.ycor() <= block_a.ycor() + 120 \
                and block_a.xcor() - 60 <= ball.xcor() <= block_a.xcor() + 60:
            ball.dx = -ball.dx
            HP[0] += -1
            print(HP[0], noBlocks)
    if destroys[1]:
        if block_b.ycor() - 120 <= ball.ycor() <= block_b.ycor() + 120 \
                and block_b.xcor() - 60 <= ball.xcor() <= block_b.xcor() + 60:
            ball.dx = -ball.dx
            HP[1] += -1
            print(HP[1], noBlocks)
    if destroys[2]:
        if block_c.ycor() - 50 <= ball.ycor() <= block_c.ycor() + 50 \
                and block_c.xcor() - 110 <= ball.xcor() <= block_c.xcor() + 110:
            ball.dx = -ball.dx
            HP[2] += -1
            print(HP[2], noBlocks)
    if destroys[3]:
        if block_d.ycor() - 70 <= ball.ycor() <= block_d.ycor() + 70 \
                and block_d.xcor() - 35 <= ball.xcor() <= block_d.xcor() + 35:
            ball.dx = -ball.dx
            HP[3] += -1
            print(HP[3], noBlocks)
    if destroys[4]:
        if block_e.ycor() - 70 <= ball.ycor() <= block_e.ycor() + 70 \
                and block_e.xcor() - 35 <= ball.xcor() <= block_e.xcor() + 35:
            ball.dx = -ball.dx
            HP[4] += -1
            print(HP[4], noBlocks)
    if destroys[5]:
        if block_f.ycor() - 70 <= ball.ycor() <= block_f.ycor() + 70 \
                and block_f.xcor() - 35 <= ball.xcor() <= block_f.xcor() + 35:
            ball.dx = -ball.dx
            HP[5] += -1
            print(HP[5], noBlocks)
    if destroys[6]:
        if block_g.ycor() - 70 <= ball.ycor() <= block_g.ycor() + 70 \
                and block_g.xcor() - 35 <= ball.xcor() <= block_g.xcor() + 35:
            ball.dx = -ball.dx
            HP[6] += -1
            print(HP[6], noBlocks)
    for i in range(len(blocks) - 1):
        if destroys[i]:
            if HP[i] == 0:
                blocks[i].reset()
                destroys[i] = False
                blocks[i].speed(0)
                blocks[i].goto(0, 350)
    # endregion
    if HP[0] == 0 and HP[1] == 0 and HP[2] == 3 and HP[3] == 0 and HP[4] == 0 and HP[5] == 0 and HP[6] == 0 and \
            HP[7] == 0:
        noBlocks = True

game.mainloop()
