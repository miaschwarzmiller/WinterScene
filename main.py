
import turtle
import random
screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t=turtle.Turtle()

t_ground = turtle.Turtle()
t_ground.speed(0)
t.speed(0)
t_ground.fillcolor("snow1")
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.end_fill()

 #cabin rectangle
t.penup()
t.goto(0, 200)
t.pendown()
t.write("Merry Christmas", align="center", font=("Arial", 30, "normal"))
#square
t.penup()
t.goto(0,-80)
t.fillcolor('brown')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
 #triangle roof
t.penup()
t.goto(0,-80)
t.pendown()
t.begin_fill()
t.goto(100,-80)
t.goto(50,-20)
t.goto(0,-80)
t.end_fill()
t.hideturtle()
t.penup()

t.goto(0, 50)


#tree
t.penup()
t.goto(195,00)
t.pendown()
t.fillcolor('DarkGreen')
t.pencolor('DarkGreen')
t.begin_fill()
t.goto(100,-150)
t.goto(290,-150)
t.goto(195,0)
t.end_fill()

t.penup()
t.goto(195,70)
t.pendown()
t.begin_fill()
t.goto(125,-50)
t.goto(265,-50)
t.goto(195,70)
t.end_fill()

t.penup()
t.goto(195,100)
t.pendown()
t.begin_fill()
t.goto(150,30)
t.goto(240,30)
t.goto(195,100)
t.end_fill()

t.pencolor('DarkGreen')
t.penup()
t.goto(170,30)
t.pendown()
t.goto(220,30)

t.penup()
t.goto(160,-50)
t.pendown()
t.goto(230,-50)
t.penup()
t.goto(185, -175)
t.fillcolor('BurlyWood4')
t.pendown()
t.begin_fill()
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.end_fill()
t.pencolor('magenta')
t.penup()
t.goto(175,-210)
t.setheading(0)
t.pendown()
t.fillcolor('magenta')
t.begin_fill()
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.end_fill()

t.pencolor('black')
t.pensize(6)
t.setheading(270)
t.penup()
t.goto(155,-170)
t.pendown()
t.forward(40)

t.setheading(0)
t.penup()
t.goto(50,-190)
t.pendown()
t.forward(40)
t.penup()
t.pencolor('snow')
t.goto(-100,300)
t.pensize(50)
t.dot()
t.penup()
t.pencolor('snow')
t.goto(-40,300)
t.pensize(50)
t.dot()
t.penup()
t.pencolor('snow')
t.goto(20,300)
t.pensize(50)
t.dot()

snow = turtle.Turtle()
snow.pensize(3)
snow.pencolor('black')
snow.speed(0)
snow.penup()
snow.goto(-200,-200)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(50)
snow.end_fill()
snow.penup()
snow.goto(-200,-100)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(35)
snow.end_fill()
snow.penup()
snow.goto(-200,-30)
snow.pendown()
snow.fillcolor('white')
snow.begin_fill()
snow.circle(25)
snow.end_fill()
snow.end_fill()
####################### HAT ############
hat =turtle.Turtle()
hat.speed(0)
hat.pencolor('black')
hat.fillcolor('black')
hat.penup()
hat.goto(-100,60)
hat.pendown()
hat.begin_fill()
hat.goto(-60,98)
hat.goto(20,98)
hat.goto(20,110)
hat.goto(-60,110)
hat.goto(-60,98)
hat.end_fill()
hat.penup()
hat.goto(-50,110)
hat.pendown()
hat.begin_fill()
hat.goto(-50,140)
hat.goto(5,140)
hat.goto(5,110)
hat.goto(-50,110)
hat.end_fill()
hat.hideturtle()

    #wreath
t.penup()
t.goto(-100, 0)
t.pendown()
t.pencolor('green')

t.circle(45)

t.pensize(5)
for i in range(500):
    t.pencolor('snow')
    x= random.randint(-1000,1000)
    y = random.randint(-100,600)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot()





turtle.done()