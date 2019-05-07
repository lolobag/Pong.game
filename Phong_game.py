# Simple pong game

import turtle

# wn shortcut for window

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
puddle_a = turtle.Turtle()
puddle_a.speed(0)
puddle_a.shape("square")
puddle_a.color("white")
puddle_a.shapesize(stretch_wid=5, stretch_len=1)
puddle_a.penup()
puddle_a.goto(-350, 0)

# Paddle B
puddle_b = turtle.Turtle()
puddle_b.speed(0)
puddle_b.shape("square")
puddle_b.color("white")
puddle_b.shapesize(stretch_wid=5, stretch_len=1)
puddle_b.penup()
puddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1


# Function
def puddle_a_up():
    y = puddle_a.ycor()
    y += 20
    puddle_a.sety(y)

def puddle_a_down():
    y = puddle_a.ycor()
    y -= 20
    puddle_a.sety(y)

def puddle_b_up():
    y = puddle_b.ycor()
    y += 20
    puddle_b.sety(y)

def puddle_b_down():
    y = puddle_b.ycor()
    y -= 20
    puddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(puddle_a_up, "w")
wn.onkeypress(puddle_a_down, "e")
wn.onkeypress(puddle_b_up, "Up")
wn.onkeypress(puddle_b_down, "Down")




# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

