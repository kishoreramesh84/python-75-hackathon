import turtle
from turtle import *
from random import randint
wn=turtle.Screen()
wn.bgcolor("light yellow")
wn.title("Race")
turtle.pencolor("dark blue")
penup()
goto(-200,200)
write("RACE TRACK!!",align='center')
goto(-160,160)
for s in range(16):
    write(s)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
sub=100
p=int(input("Enter no of participants:"))
a=[0 for i in range(p)]
c=[0 for i in range(p)]
for i in range(p):
    a[i]=Turtle()
    c[i]=input("enter color:")
    a[i].color(c[i])
    a[i].shape('turtle')
    a[i].penup()
    a[i].goto(-160,sub)
    a[i].pendown()
    sub=sub-30
for turn in range(100):
    for i in range(p):
        a[i].forward(randint(1,5))
max=a[0].pos()
index=0
for i in range(p):
    if(a[i].pos()>max):
        max=a[i].pos()
        index=i
print("THE WINNER IS ",c[index])