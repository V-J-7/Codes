p=int(input("Enter the angle:-"))
import turtle
turtle.speed(10000000)
turtle.bgcolor("black")
t=turtle.Turtle()
t.pensize(10)
t.speed(0)
a=["red","cyan","blue","green","yellow","indigo"]
for x in range(3600):
    t.pencolor(a[x%6])
    t.forward(x*1)
    t.left(p)
    
