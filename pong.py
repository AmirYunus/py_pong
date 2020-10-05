import turtle
import time
import random
import os

# Function
def ball_speed():
    r = random.uniform(-1,1)
    if r > 0:
        r = random.uniform(.1,.2)
    else:
        r = random.uniform(-.2,-.1)
    return r

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

def countdown():
    count.write("3", align="center", font=("IBM Plex Mono", 24, "normal"))
    time.sleep(1)
    count.clear()
    count.write("2", align="center", font=("IBM Plex Mono", 24, "normal"))
    time.sleep(1)
    count.clear()
    count.write("1", align="center", font=("IBM Plex Mono", 24, "normal"))
    time.sleep(1)
    count.clear()

# Window set up
window = turtle.Screen()
window.title("py_pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
left_score = 0
right_score = 0

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.delta_x = ball_speed()
ball.delta_y = ball_speed()

# Score board
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player A: {left_score}  Player B: {right_score}", align="center", font=("IBM Plex Mono", 24, "normal"))

# Countdown
count = turtle.Turtle()
count.speed(0)
count.color("white")
count.penup()
count.hideturtle()
count.goto(0, 0)

# Keyboard binding
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.delta_x)
    ball.sety(ball.ycor() + ball.delta_y)

    # Ball movement (border)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.delta_y *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.delta_y *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 410:
        left_score += 1
        score.clear()
        if left_score - right_score >= 3:
            score.write(f"Player A wins!", align="center", font=("IBM Plex Mono", 24, "normal"))
            os.system("aplay fanfare.wav&")
            ball.goto(0,0)
            ball.delta_x = 0
            ball.delta_y = 0
        else:
            score.write(f"Player A: {left_score}  Player B: {right_score}", align="center", font=("IBM Plex Mono", 24, "normal"))
            countdown()
            ball.goto(0,0)
            ball.delta_x = ball_speed()
            ball.delta_y = ball_speed()

    if ball.xcor() < -410:
        right_score += 1
        score.clear()
        if right_score - left_score >= 3:
            score.write(f"Player B wins!", align="center", font=("IBM Plex Mono", 24, "normal"))
            os.system("aplay fanfare.wav&")
            ball.goto(0,0)
            ball.delta_x = 0
            ball.delta_y = 0
        else:
            score.write(f"Player A: {left_score}  Player B: {right_score}", align="center", font=("IBM Plex Mono", 24, "normal"))
            countdown()
            ball.goto(0,0)
            ball.delta_x = ball_speed()
            ball.delta_y = ball_speed()

    # Ball movement (paddle collision)
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and  ball.ycor() > right_paddle.ycor() -40):
        ball.setx(330)
        ball.delta_x *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and  ball.ycor() > left_paddle.ycor() -40):
        ball.setx(-330)
        ball.delta_x *= -1
        os.system("aplay bounce.wav&")
