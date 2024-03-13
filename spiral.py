import turtle
import random
screen=turtle.Screen()
screen.setup(width=1.0,height=1.0)
a=["red","blue","cyan","yellow","sky blue","white"]
turtle.pensize(4)
turtle.penup()
turtle.goto(0,-400)
turtle.pendown()
turtle.bgcolor("black")
turtle.speed(11)
for x in range(10000000000000):
    turtle.circle(x*2)
    turtle.pencolor(random.choice(a))
