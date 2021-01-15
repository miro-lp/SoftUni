import turtle
import game
import time

SIZE = 20
game = game.Game()

screen = turtle.Screen()
screen.title("PONG GAME")
screen.setup(game.width, game.high)
screen.bgcolor("Black")
screen.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()

paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.shapesize(game.paddle_height / 20, game.paddle_width / 20)
paddle_a.color("white")
paddle_a.penup()

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.shapesize(game.paddle_height / 20, game.paddle_width / 20)
paddle_b.color("white")
paddle_b.penup()

text = turtle.Turtle()
text.color("Green")
text.penup()
text.goto(0, game.high / 2 - 40)
text.write("Player A: 0, Player B: 0", align="center", font=("Gothic", 20, "bold"))
text.hideturtle()

screen.listen()
screen.onkeypress(game.paddle_a_up, "w")
screen.onkeypress(game.paddle_a_down, "s")
screen.onkeypress(game.paddle_b_up, "Up")
screen.onkeypress(game.paddle_b_down, "Down")

prev_points_a = None
prev_points_b = None

while True:
    game.tick()
    ball.goto(game.ball_pos())
    paddle_a.goto(game.paddle_a_pos)
    paddle_b.goto(game.paddle_b_pos)
    if prev_points_a!=game.points_a or prev_points_b!=game.points_b:
        text.clear()
        text.write(f"Player A: {game.points_a}, Player B: {game.points_b}", align="center", font=("Gothic", 20, "bold"))
    prev_points_a = game.points_a
    prev_points_b = game.points_b
    screen.update()
    time.sleep(.001)
