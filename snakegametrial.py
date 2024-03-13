print("Press w to turn downwards \n Press s to turn upwards")
import turtle
import random
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
turtle.bgcolor("black")
snake=turtle.Turtle()
snake.pencolor("white")
food=turtle.Turtle()
food.hideturtle()
food.pencolor("yellow")
snake.pensize(4)
food.speed(20)
def loop():
    for x in range(10):
        food.penup()
        food.goto(random.randrange(-500,500),random.randrange(-499,499))
        food.pendown()
        food.begin_fill()
        food.fillcolor("yellow")
        for d in range(5):
            food.forward(20)
            food.left(144)
        food.end_fill()
loop()
def a():
    snake.left(30)
def d():
    snake.right(90)
def s():
    snake.right(30)
turtle.listen()
turtle.onkey(a,'w')
turtle.onkey(d,'a')
turtle.onkey(s,'s')
while True:
    snake.forward(1)
