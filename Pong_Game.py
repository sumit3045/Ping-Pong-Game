import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong bt @sumit3045")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer() #Stops the window from updating, speeds up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() #Capital Turtle is class name
paddle_a.speed(0) #Max possilbe speed of the paddle apearing is 0
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #By default, the shape of the pong is 20 pixels by 20 pixels
paddle_a.penup() #Turtles draw a line as they're moving. so we dont need to draw a line hence penup used
paddle_a.goto(-350,0) #-350 is x-cordinate and 0 is y-cordinate




# Paddle B
paddle_b = turtle.Turtle() #Capital Turtle is class name
paddle_b.speed(0) #Max possilbe speed of the paddle apearing is 0
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #By default, the shape of the pong is 20 pixels by 20 pixels
paddle_b.penup() #Turtles draw a line as they're moving. so we dont need to draw a line hence penup used
paddle_b.goto(350,0) #350 is x-cordinate and 0 is y-cordinate

# Ball
ball = turtle.Turtle() #Capital Turtle is class name
ball.speed(0) #Max possilbe speed of the paddle apearing is 0
ball.shape("circle")
ball.color("white")
ball.penup() #Turtles draw a line as they're moving. so we dont need to draw a line hence penup used
ball.goto(0,0) #-350 is x-cordinate and 0 is y-cordinate
ball.dx = 4 # Means it will move the ball pixel by 2 pixels
ball.dy = 4 # Means it will move the ball pixel by 2 pixels

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # We write this because we dont want to draw a line when the pen moves
pen.hideturtle() # Hiding the turtle
pen.goto(0, 260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal")) # Normal can be set to bold



#Function

def paddle_a_up():
    y= paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y= paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen() #Listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # This reverses the direction of the ball in motion
        winsound.PlaySound("irfan_one_more.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("irfan_one_more.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0) # Places the ball at center
        ball.dx *= -1 # Reverse Direction
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("irfan_easy_boy.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("irfan_easy_boy.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40 ):
        ball.setx(-340)
        ball.dx *= -1
