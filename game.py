import turtle
from random import choice
# region blocks
blocks = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
          turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), 0, 0]
HP = [3, 3, 3, 3, 3, 3, 3]
destroys = [True, True, True, True, True, True, True, True]
collision = [True, True, True, True, True, True, True, True]
checkers = [False, True, True, False]
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

hearts = [turtle.Turtle(visible=False), turtle.Turtle(visible=False), turtle.Turtle(visible=False),
          turtle.Turtle(visible=False), turtle.Turtle(visible=False), turtle.Turtle(visible=False)]
heart_builder(hearts[0], -450, 280)
heart_builder(hearts[1], -400, 280)
heart_builder(hearts[2], -350, 280)
heart_builder(hearts[3], 490, 280)
heart_builder(hearts[4], 440, 280)
heart_builder(hearts[5], 390, 280)
# endregion
# region winner text
FONT = ("Arial", 44)
winner = turtle.Turtle(visible=False)
winner.color("white")
winner.penup()
winner.setposition(-250, 0)
winner.write(blocks[11], font=FONT)
winner.clear()
# endregion
# region functions
def move_up_left():
    y = blocks[9].ycor()
    if y > 240:
        y = 240
    blocks[9].sety(y + 10)
def move_down_left():
    y = blocks[9].ycor()
    if y < -240:
        y = -240
    blocks[9].sety(y - 10)
def move_up_right():
    y = blocks[10].ycor()
    if y > 240:
        y = 240
    blocks[10].sety(y + 10)
def move_down_right():
    y = blocks[10].ycor()
    if y < -240:
        y = -240
    blocks[10].sety(y - 10)
def clear():
    for j in range(len(blocks)):
        blocks[i].color("gray")
def ballReset(n, x, y):
    blocks[n].goto(x, y)
    blocks[n].dx = choice([-4, -3, -2, 2, 3, 4])
    blocks[n].dy = choice([-4, -3, -2, 2, 3, 4])
def showWinner(x, y, text):
    winner.penup()
    winner.goto(x, y)
    winner.write(text, font=FONT)

def wallsCollision(num, trigger, checker, cor, ballId, reset):
    if cor == "y":
        if blocks[num].ycor() >= trigger or blocks[num].ycor() <= -trigger:
            checkers[checker] = True
            blocks[num].dy = -blocks[num].dy
    elif cor == "x":
        if blocks[num].xcor() >= trigger:
            checkers[checker] = True
            blocks[12] -= -1
            if blocks[12] == 1:
                hearts[5].clear()
            elif blocks[12] == 2:
                hearts[4].clear()
            elif blocks[12] == 3:
                hearts[3].clear()
                clear()
                showWinner(-500, 0, "player left win")
                checkers[3] = True
            if reset:
                ballReset(ballId, 0, 0)
        if blocks[num].xcor() <= -trigger:
            checkers[checker] = True
            blocks[11] -= -1
            if blocks[11] == 1:
                hearts[2].clear()
            elif blocks[11] == 2:
                hearts[1].clear()
            elif blocks[11] == 3:
                hearts[0].clear()
                clear()
                showWinner(0, 0, "player right win")
                checkers[3] = True
            if reset:
                ballReset(ballId, 0, 0)

def blockBuilder(num, color, x, y, shape, gx, gy, check):
    blocks[num].color(color)
    blocks[num].speed(10)
    blocks[num].shape(shape)
    if check:
        blocks[num].shapesize(x, y)
    else:
        blocks[num].dx = choice([-4, -3, -2, 2, 3, 4])
        blocks[num].dy = choice([-4, -3, -2, 2, 3, 4])
    blocks[num].penup()
    blocks[num].goto(gx, gy)

def blockCollision(i):
    for a in range(len(collision)):
        if a != i:
            collision[a] = True
# endregion
# region blocks
blockBuilder(0, "white", 10, 5, "square", 0, 200, True)
blockBuilder(1, "white", 10, 5, "square", 0, -200, True)
blockBuilder(2, "white", 5, 10, "square", 0, 0, True)
blockBuilder(3, "white", 4, 2, "square", 150, 60, True)
blockBuilder(4, "white", 4, 2, "square", -150, 60, True)
blockBuilder(5, "white", 4, 2, "square", -150, -60, True)
blockBuilder(6, "white", 4, 2, "square", 150, -60, True)
blockBuilder(7, "red", 0, 0, "circle", -400, 0, False)
blockBuilder(8, "black", 0, 0, "circle", 400, 0, False)
blockBuilder(9, "white", 5, 1, "square", -450, 0, True)
blockBuilder(10, "white", 5, 1, "square", 450, 0, True)
# endregion
# region buttons
game.listen()
game.onkeypress(move_up_left, "w")
game.onkeypress(move_down_left, "s")
game.onkeypress(move_up_right, "Up")
game.onkeypress(move_down_right, "Down")
# endregion
while True:
    game.update()
    if not checkers[3]:
        blocks[7].setx(blocks[7].xcor() + blocks[7].dx)
        blocks[7].sety(blocks[7].ycor() + blocks[7].dy)
        blocks[8].setx(blocks[8].xcor() + blocks[8].dx)
        blocks[8].sety(blocks[8].ycor() + blocks[8].dy)
        # region balls
        if blocks[8].ycor() + 20 >= blocks[7].ycor() >= blocks[8].ycor() - 20 and blocks[8].xcor() + 20 >= \
                blocks[7].xcor() >= blocks[8].xcor() - 20:
            if checkers[1]:
                blocks[7].dx = -blocks[7].dx
                checkers[1] = False

        if blocks[7].ycor() + 20 >= blocks[8].ycor() >= blocks[7].ycor() - 20 and blocks[7].xcor() + 20 >= \
                blocks[8].xcor() >= blocks[7].xcor() - 20:
            if checkers[2]:
                blocks[8].dx = -blocks[8].dx
                checkers[2] = False
        wallsCollision(7, 290, 1, "y", 7, False)
        wallsCollision(7, 490, 1, "x", 7, True)
        wallsCollision(7, 490, 1, "x", 7, True)
        wallsCollision(8, 290, 2, "y", 8, False)
        wallsCollision(8, 490, 2, "x", 8, True)
        wallsCollision(8, 490, 2, "x", 8, True)
        # endregion
        # region beat off
        if blocks[10].ycor() - 60 <= blocks[7].ycor() <= blocks[10].ycor() + 60 \
                and blocks[10].xcor() - 20 <= blocks[7].xcor() <= blocks[10].xcor() + 20:
            blocks[7].dx = -blocks[7].dx
        if blocks[9].ycor() - 60 <= blocks[7].ycor() <= blocks[9].ycor() + 60 \
                and blocks[9].xcor() - 20 <= blocks[7].xcor() <= blocks[9].xcor() + 20:
            blocks[7].dx = -blocks[7].dx
        if blocks[10].ycor() - 50 <= blocks[8].ycor() <= blocks[10].ycor() + 50 \
                and blocks[10].xcor() - 20 <= blocks[8].xcor() <= blocks[10].xcor() + 20:
            blocks[8].dx = -blocks[8].dx
        if blocks[9].ycor() - 50 <= blocks[8].ycor() <= blocks[9].ycor() + 50 \
                and blocks[9].xcor() - 20 <= blocks[8].xcor() <= blocks[9].xcor() + 20:
            blocks[8].dx = -blocks[8].dx
        # endregion
        # region hp
        for i in range(len(HP)):
            if destroys[i]:
                if i < 2:
                    if blocks[i].ycor() - 120 <= blocks[8].ycor() <= blocks[i].ycor() + 120 \
                            and blocks[i].xcor() - 60 <= blocks[8].xcor() <= blocks[i].xcor() + 60:
                        blocks[8].dx = -blocks[8].dx
                        HP[i] += -1
                    if blocks[i].ycor() - 120 <= blocks[7].ycor() <= blocks[i].ycor() + 120 \
                            and blocks[i].xcor() - 60 <= blocks[7].xcor() <= blocks[i].xcor() + 60:
                        blocks[7].dx = -blocks[7].dx
                        HP[i] += -1
                elif i == 2:
                    if blocks[i].ycor() - 60 <= blocks[8].ycor() <= blocks[i].ycor() + 60 \
                            and blocks[i].xcor() - 120 <= blocks[8].xcor() <= blocks[i].xcor() + 120:
                        blocks[8].dx = -blocks[8].dx
                        HP[i] += -1
                    if blocks[i].ycor() - 60 <= blocks[7].ycor() <= blocks[i].ycor() + 60 \
                            and blocks[i].xcor() - 120 <= blocks[7].xcor() <= blocks[i].xcor() + 120:
                        blocks[7].dx = -blocks[7].dx
                        HP[i] += -1
                else:
                    if blocks[i].ycor() - 57 <= blocks[8].ycor() <= blocks[i].ycor() + 57 \
                            and blocks[i].xcor() - 35 <= blocks[8].xcor() <= blocks[i].xcor() + 35:
                        blocks[8].dx = -blocks[8].dx
                        HP[i] += -1
                    if blocks[i].ycor() - 57 <= blocks[7].ycor() <= blocks[i].ycor() + 57 \
                            and blocks[i].xcor() - 35 <= blocks[7].xcor() <= blocks[i].xcor() + 35:
                        blocks[7].dx = -blocks[7].dx
                        HP[i] += -1
        for i in range(len(HP)):
            if destroys[i]:
                if HP[i] == 0:
                    blocks[i].reset()
                    destroys[i] = False
                    blocks[i].speed(0)
                    blocks[i].penup()
                    blocks[i].goto(0, 350)
        # endregion
        if HP[0] == 0 and HP[1] == 0 and HP[2] == 3 and HP[3] == 0 and HP[4] == 0 and HP[5] == 0 and HP[6] == 0:
            checkers[0] = True
