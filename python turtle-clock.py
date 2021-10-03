#I try to write my code only using turtle functions.Because in my opinion the main purpose of this project is creating clock by using only turtle graphics so in my view it’s not useful to import time to make the turtle work(“i try to create my own turtle analog clock by using only turtle graphics”)
import turtle
t=turtle.Screen()
t.title("TSEGANESH_YIFRU_SECTION_1_UGR/3970")
t.setup(width=410,height=410)
#t.bgpic('img.gif')
t.bgcolor('black')
sec=turtle.Turtle()
name=turtle.Turtle()
min=turtle.Turtle()
hour=turtle.Turtle()
text=turtle.Turtle()
red=turtle.Turtle()
green=turtle.Turtle()
yellow=turtle.Turtle()
hour.hideturtle()
min.hideturtle()
sec.hideturtle()
text.hideturtle()
name.hideturtle()
min.speed(80)
text.speed(1000)
red.speed(10000)
yellow.speed(10000)
green.speed(10000)
min.pencolor('black')
hour.pencolor("red")
text.pencolor("orange")
min.pencolor("yellow")
sec.pencolor('green')
yellow.shape('circle')
red.shape('circle')
green.shape('circle')
yellow.fillcolor('yellow')
red.fillcolor('red')
green.fillcolor('green')
def name_writer():
 type=('courier',14,'bold')
 name.left(90)
 name.penup()
 name.forward(170)
 name.pendown()
 name.color('black')
 name.write("TCLOCK",font=type,align='center')
def text_writer(x=0,y=0,r=110):
 text.left(90)
 a=30
 numlist = ['፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱', '፲', '፲፩', '፲፪']
 for i in numlist:
   type=('courier',12,'bold')
   text.color('black')
   text.penup()
   text.right(a)
   text.forward(87)
   text.pendown()
   text.write(i,font=type)
   text.penup()
   text.backward(87)
def draw_circle(x=0,y=0,radius=110):
 green.pencolor('green')
 green.pensize(2.5)
 green.penup()
 green.goto(x,y-radius)
 green.pendown()
 green.circle(radius,240)
 yellow.pencolor('yellow')
 yellow.pensize(5)
 yellow.penup()
 yellow.home()
 yellow.goto(x,y-radius)
 yellow.pendown()
 yellow.circle(radius+5,240)
 red.pencolor('red')
 red.pensize(3.5)
 red.penup()
 red.home()
 red.goto(x,y-radius)
 red.pendown()
 red.circle(radius+10,240)
sec.left(90)
hour.right(60)
def clock():
 min.dot(15)
 i=0
 angle=30
 while i<=12:
   j=0
   ang=6
   while j<=60:
     min.clear()
     min.dot(15)
     min.right(ang)
     min.forward(60)
     min.backward(60)
     k=0
     angl=6
     while k<=60:
       sec.speed(1.26)
       sec.hideturtle()
       sec.forward(75)
       sec.speed(0.2)
       sec.showturtle()
       sec.speed(0.5)
       sec.hideturtle()
       sec.speed(10)
       sec.backward(75)
       sec.right(angl)
       sec.speed(80)
       sec.clear()
       k=k+1
   hour.forward(40)
   hour.backward(40)
name_writer()
text_writer()
draw_circle()
min.left(90)
sec.pensize(2)
hour.pensize(7)
min.pensize(3)
hour.forward(45)
clock()


