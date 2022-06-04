from turtle import Turtle,Screen
from Paddleclass import Paddle
from Ballclass import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

gameon=True
while gameon:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()
    if score.l_score==5 :
        print("Left player won!")
        gameon=False
    if score.r_score==5 :
        print("Right player won!")
        gameon=False
screen.exitonclick()