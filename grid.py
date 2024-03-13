import turtle
import math
t=turtle.Turtle()
b=turtle.Turtle()
turtle.speed(1000)
for x in range(100):
    for c in range(100):
        y=math.sin(x)
        t.goto(x,c*y)
        b.goto(c*y,x)
